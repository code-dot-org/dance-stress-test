import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep


class DanceStressTest(unittest.TestCase):

    def setUp(self):
        # desired_caps = {
        #     'platformName': 'Android',
        #     # 'platformVersion': '8.0',
        #     'avd': 'Nexus_4_API_22',
        #     'deviceName': 'Android Emulator',
        #     'browserName': 'Browser',
        #     'automationName': 'UiAutomator2'
        # }
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', {})
        self.driver.orientation = "LANDSCAPE"

    def tearDown(self):
        self.driver.quit()

    def testStress(self):
        # Load dance party free-play level
        self.driver.get('https://test-studio.code.org/s/dance/stage/1/puzzle/13')

        # Enter age and dismiss dialog, which causes a page reload
        self.bypassAgeDialog()

        # Run basic dance party for 30 seconds
        self.waitToSee('runButton')
        self.clickRun()
        sleep(30)
        self.clickReset()
        sleep(1)
        self.assertTrue(self.isNotRunning())

        # TODO: Load all characters
        # TODO: Play all dances
        # TODO: Run/reset several times to catch memory leaks
        # TODO: Force out-of-memory to see what happens

    def bypassAgeDialog(self):
        self.waitToSee('uitest-age-selector')
        selector = Select(self.driver.find_element_by_id('uitest-age-selector'))
        selector.select_by_visible_text('10')
        submit = self.driver.find_element_by_id('uitest-submit-age')
        submit.click()
        sleep(3)  # Enough time for reload to start

    def clickRun(self):
        el = self.driver.find_element_by_id('runButton')
        el.click()

    def clickReset(self):
        el = self.driver.find_element_by_id('resetButton')
        el.click()

    def isNotRunning(self):
        el = self.driver.find_element_by_id('runButton')
        return el.is_displayed() and el.is_enabled()

    def waitToSee(self, element_id):
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


# Start of script
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DanceStressTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
