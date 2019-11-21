from datetime import datetime
import json
import os
from time import sleep


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
        """
        print('-- Running {program_name} for {run_duration} seconds {repeat_runs} times --'.format(
            program_name=program_name, run_duration=run_duration, repeat_runs=repeat_runs
        ))
        """

        #self.load_free_play()
        #self.set_blocks(block_xml)

        self.driver_state.driver.get('{origin}s/oceans/stage/1/puzzle/2'.format(origin=self.driver_state.origin))
        sleep(30)

        # Several runs in a row

        """
        for i in range(repeat_runs):
            self.click_run()
            sleep(run_duration)
            self.capture_timing_data(program_name, run_number=i)
            if i == repeat_runs - 1:
                self.screenshot(program_name)
            self.click_reset()
            sleep(0.5)
        """
