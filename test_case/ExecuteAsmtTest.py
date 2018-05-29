"""
Test student execute different assignments.

  includes: gp, ip, qa
"""
from models.StudentTest import StudentTest
import models.function as fun
import time


class ExecuteAsmtTest(StudentTest):
    """Executed assignments test."""

    def test_ip_asmt_execute(self):
        """Test execute new individual assignment."""
        title = fun.enter_course(self.driver, "13StableGeneralCourse")
        self.assertEqual(
            title,
            "13stablegen: 13StableGeneralvideoassignments"
        )
        self.__get_asmt_list_info()
        fun.found_asmt_by_page(self.driver, "0001_Ren_GP")

    def __get_asmt_list_info(self):
        """Only can be used after enter course."""
        for handle in self.driver.window_handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to_window(handle)
                time.sleep(5)
