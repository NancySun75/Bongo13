"""Teacher delete the specific assignment."""
from models.TeacherTest import TeacherTest
import models.function as fun
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DeleteAsmtTest(TeacherTest):
    """Delete specific assignment."""

    def test_execute_delete(self):
        """Execute delete operation for found assignment."""
        title = fun.enter_course(self.driver, "bigbengenerallink")
        self.assertEqual(
            title,
            "bigbengenerallink: videoassignments"
        )
        self.asmt_list = self.__get_asmt_list_info()
        delete_asmt_file = open('data/to_delete_asmt.txt', 'r')
        lines = delete_asmt_file.readlines()
        delete_asmt_file.close()

        for line in lines:
            name = line.replace('\n', '')
            print name
            fun.delete_asmt(self.driver, self.asmt_list['handle'], name)

    def __get_asmt_list_info(self):
        """Only can be used after enter course."""
        for handle in self.driver.window_handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to_window(handle)
                condition = expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, "[aria-label='Add New Item']")
                )
                WebDriverWait(self.driver, 60, 0.5).until(condition)
                return {'handle': handle, 'url': self.driver.current_url}
