"""Test teacher cases."""
import unittest
from test_case.models.driver import chrome
from test_case.models.function import login_bongo


class TeacherTest(unittest.TestCase):
    """Prepare for teacher test."""

    def setUp(self):
        """Prepare driver and login as teacher."""
        self.driver = chrome()
        login_bongo(self.driver, "educator-1", "!QAZ2wsx")

    def tearDown(self):
        """Quit driver (close browser)."""
        self.driver.quit()
