"""Test student cases."""
import unittest
from test_case.models.driver import chrome
from test_case.models.function import login_bigben


class StudentTest(unittest.TestCase):
    """Prepare for student test."""

    def setUp(self):
        """Prepare driver and login as student."""
        self.driver = chrome()
        login_bigben(self.driver, "student-1", "!QAZ2wsx")

    def tearDown(self):
        """Quit driver (close browser)."""
        self.driver.quit()
