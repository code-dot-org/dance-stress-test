import unittest
from driver import DriverState
from ml_hoc_page import MlHocPage


class MlHocStressTest(unittest.TestCase):
    def setUp(self):
        #self.page = MlHocPage(driver_state=DriverState(origin='https://studio.code.org/', framework='selenium'))
        self.page = MlHocPage(driver_state=DriverState(origin='https://code-dot-org.github.io/ml-activities?guide=off', framework='selenium'))
        self.page.setup()

    def tearDown(self):
        self.page.teardown()

    def testCase1(self):
        self.page.run_program()

