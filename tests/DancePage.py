import os
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep


# Wrapper around an appium interface to a Dance Party page for readable tests
class DancePage:
    def __init__(self, origin='https://test-studio.code.org/'):
        self.origin = origin
        self.driver = None
        self.screenshot_folder = None

    def setup(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', {})
        self.driver.orientation = "LANDSCAPE"
        self.screenshot_folder = os.getenv('SCREENSHOT_PATH', '/tmp')

        # TODO: Figure out local testing
        # desired_caps = {
        #     'platformName': 'Android',
        #     # 'platformVersion': '8.0',
        #     'avd': 'Nexus_4_API_22',
        #     'deviceName': 'Android Emulator',
        #     'browserName': 'Browser',
        #     'automationName': 'UiAutomator2'
        # }
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown(self):
        self.driver.quit()

    def run_fixture(self, xml_filename, run_duration=15, repeat_runs=1):
        block_xml = load_xml(xml_filename)
        self.run_program(block_xml, xml_filename, run_duration, repeat_runs)

    def run_program(self, block_xml, program_name, run_duration=15, repeat_runs=1):
        print('-- Running {program_name} for {run_duration} seconds {repeat_runs} times --'.format(
            program_name=program_name, run_duration=run_duration, repeat_runs=repeat_runs
        ))

        self.load_free_play()
        self.set_blocks(block_xml)

        # Several runs in a row
        for i in range(repeat_runs):
            self.click_run()
            sleep(run_duration)
            self.capture_framerate(program_name, run_number=i)
            if i == repeat_runs - 1:
                self.screenshot(program_name)
            self.click_reset()
            sleep(0.5)

    def load_free_play(self):
        # Load dance party free-play level
        self.driver.get('{origin}s/dance/stage/1/puzzle/13'.format(origin=self.origin))

        # Enter age and dismiss dialog, which causes a page reload
        self.bypass_age_dialog()

        # Wait for the page to load again
        self.wait_to_see('runButton')

        # Hide footer (at some resolutions it covers the run button)
        self.hide_footer()

    def bypass_age_dialog(self):
        self.wait_to_see('uitest-age-selector')
        selector = Select(self.driver.find_element_by_id('uitest-age-selector'))
        selector.select_by_visible_text('10')
        submit = self.driver.find_element_by_id('uitest-submit-age')
        submit.click()
        sleep(3)  # Enough time for reload to start

    def hide_footer(self):
        self.driver.execute_script("""
            document.querySelector('#page-small-footer').style.display = 'none';
        """)

    def set_blocks(self, block_xml):
        self.driver.execute_script("""
            var blocksXml = arguments[0];
            Blockly.mainBlockSpace.clear();
            var arrangedBlocksXml = __TestInterface.arrangeBlockPosition(blocksXml, {});
            __TestInterface.loadBlocks(arrangedBlocksXml);
        """, block_xml)

    def click_run(self):
        el = self.driver.find_element_by_id('runButton')
        el.click()

    def click_reset(self):
        el = self.driver.find_element_by_id('resetButton')
        el.click()

    def is_not_running(self):
        el = self.driver.find_element_by_id('runButton')
        return el.is_displayed() and el.is_enabled()

    def wait_to_see(self, element_id):
        element = None
        attempt_count = 0
        while element is None:
            try:
                attempt_count += 1
                element = self.driver.find_element_by_id(element_id)
            except NoSuchElementException:
                if attempt_count > 30:
                    print('Could not locate element #{} in 30 attempts'.format(element_id))
                    raise
                else:
                    sleep(1)  # Wait one second then check again

    def screenshot(self, name):
        self.driver.save_screenshot(self.screenshot_folder + '/' + name + '.png')

    def capture_framerate(self, program_name, run_number):
        framerate = self.driver.execute_script("""
            return __TestInterface.frameRate && __TestInterface.frameRate();
        """) or 'unknown'
        print('{program_name} | {run_number} | framerate | {framerate}'.format(
            program_name=program_name, run_number=run_number, framerate=framerate
        ))


#
# Static helpers
#


def load_xml(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename))
    contents = f.read()
    f.close()
    return contents
