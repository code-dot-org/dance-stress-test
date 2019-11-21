import os
from time import sleep
import appium
import selenium
from selenium.common.exceptions import NoSuchElementException


class DriverState:
    def __init__(self, origin, framework='appium'):
        self.origin = origin
        self.driver = None
        self.screenshot_folder = None
        self.artifact_folder = None
        self.framework = framework

    def setup(self):
        desired_caps = {}
        if os.environ.get('DEVICEFARM_DEVICE_PLATFORM_NAME', 'unknown') == 'iOS':
            desired_caps = {
                'platformName': 'iOS',
                'platformVersion': '11.4',
                'deviceName': 'iPhone 7',
                'browserName': 'Safari',
            }
        if self.framework == 'appium':
            self.driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self.driver.orientation = "LANDSCAPE"
        elif self.framework == 'selenium':
            self.driver = selenium.webdriver.Chrome()
        else:
            raise ValueError('Unsupported driver "{}"'.format(self.framework))

        self.screenshot_folder = os.getenv('SCREENSHOT_PATH', '/tmp')
        self.artifact_folder = os.getenv('DEVICEFARM_LOG_DIR', '/tmp')

    def teardown(self):
        self.driver.quit()

    def wait_to_see(self, find_fn):
        element = None
        attempt_count = 0
        while element is None:
            try:
                attempt_count += 1
                #element = self.driver.find_element_by_id(element_id)
                element = find_fn(self.driver)
            except NoSuchElementException:
                if attempt_count > 30:
                    print('Could not locate element in 30 attempts')
                    raise
                else:
                    sleep(1)  # Wait one second then check again
        return element
