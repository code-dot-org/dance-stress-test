import unittest
import pytest
from driver import DriverState
from ml_hoc_page import MlHocPage


# TODO: migrate to pytest
@pytest.mark.usefixtures('framework')
@pytest.mark.usefixtures('ml_hoc_url')
class MlHocStressTest(unittest.TestCase):
    def setUp(self):
        self.page = MlHocPage(driver_state=DriverState(origin=self.ml_hoc_url, framework=self.framework))
        self.page.setup()

    def tearDown(self):
        self.page.teardown()

    def testCase1(self):
        self.page.run_program()

