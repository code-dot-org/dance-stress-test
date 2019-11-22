from datetime import datetime
import json
import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException


# Wrapper around an appium interface to a Dance Party page for readable tests
class MlHocPage:
    def __init__(self, driver_state):
        self.driver_state = driver_state

    def setup(self):
        self.driver_state.setup()

    def teardown(self):
        self.driver_state.teardown()

    def run_program(self):
        print('Running program')

        # Fish vs. Trash training screen
        self.driver_state.driver.get('{}/s/oceans/stage/1/puzzle/{}?guide=off'.format(self.driver_state.origin, 2))
        fish_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Fish'))
        not_fish_button = _find_button_by_text(self.driver_state.driver, 'Not Fish')
        for i in range(0, 3):
            fish_button.click()
            sleep(1)
            not_fish_button.click()
            sleep(1)
        _find_button_by_text(self.driver_state.driver, 'Continue').click()

        # Fish vs. Trash sorting screen
        run_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Run'))
        run_button.click()
        continue_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Continue'))
        continue_button.click()

        # Fish vs. Trash pond screen
        continue_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Continue'))
        sleep(2)

        # Sea Creatures initial screen
        # Request page via URL instead of clicking continue button so we can set guide=off param
        self.driver_state.driver.get('{}/s/oceans/stage/1/puzzle/{}?guide=off'.format(self.driver_state.origin, 3))
        run_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Run'))
        run_button.click()
        continue_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Continue'))
        sleep(2)

        # Sea Creatures training screen
        self.driver_state.driver.get('{}/s/oceans/stage/1/puzzle/{}?guide=off'.format(self.driver_state.origin, 4))
        yes_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Yes'))
        no_button = _find_button_by_text(self.driver_state.driver, 'No')
        for i in range(0, 3):
            yes_button.click()
            sleep(1)
            no_button.click()
            sleep(1)
        _find_button_by_text(self.driver_state.driver, 'Continue').click()

        # Sea Creatures sorting screen
        run_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Run'))
        run_button.click()
        continue_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Continue'))
        continue_button.click()

        # Sea Creatures pond screen
        continue_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Continue'))
        sleep(2)

        # Short words screen
        self.driver_state.driver.get('{}/s/oceans/stage/1/puzzle/{}?guide=off'.format(self.driver_state.origin, 6))
        short_word = 'Blue'
        word_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, short_word))
        word_button.click()

        # Short words training screen
        yes_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, short_word))
        no_button = _find_button_by_text(self.driver_state.driver, 'Not ' + short_word)
        for i in range(0, 3):
            yes_button.click()
            sleep(1)
            no_button.click()
            sleep(1)
        _find_button_by_text(self.driver_state.driver, 'Continue').click()

        # Short words sorting screen
        run_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Run'))
        run_button.click()
        continue_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Continue'))
        continue_button.click()

        # Short words pond screen
        continue_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Continue'))
        sleep(2)

        # Long words screen
        self.driver_state.driver.get('{}/s/oceans/stage/1/puzzle/{}?guide=off'.format(self.driver_state.origin, 8))
        long_word = 'Fierce'
        word_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, long_word))
        word_button.click()

        # Long words training screen
        yes_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, long_word))
        no_button = _find_button_by_text(self.driver_state.driver, 'Not ' + long_word)
        for i in range(0, 3):
            yes_button.click()
            sleep(1)
            no_button.click()
            sleep(1)
        _find_button_by_text(self.driver_state.driver, 'Continue').click()

        # Long words sorting screen
        run_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Run'))
        run_button.click()
        continue_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Continue'))
        continue_button.click()

        # Long words pond screen
        finish_button = self.driver_state.wait_to_see(lambda d: _find_button_by_text(d, 'Finish'))
        sleep(10)


def _find_button_by_text(webdriver, text):
    buttons = webdriver.find_elements_by_css_selector('button')
    fish_button_list = filter(lambda e: e.text == text, buttons)
    if not fish_button_list:
        raise NoSuchElementException('No button found with text {}'.format(text))
    return fish_button_list[0]
