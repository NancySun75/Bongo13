"""
Test teacher create different assignments.

  includes: gp, ip, qa
"""
from models.TeacherTest import TeacherTest
from models.DDT import DDT
from page_obj.GPAsmtConfigPage import GPAsmtConfigPage
import models.function as fun
import time


class CreateAsmtTest(TeacherTest):
    """Create assignments test."""

    def test_gp_asmt_create(self):
        """Test create new group assignments."""
        self.data = DDT('data/gp_asmt_create.xlsx').get_data_from_file()
        title = fun.enter_course(self.driver, "bigbengenerallink")
        self.asmt_list = self.__get_asmt_list_info()
        self.assertEqual(
            title,
            "bigbengenerallink: videoassignments"
        )

        for asmt_data in self.data:
            fun.switch_to_asmt(self.driver, self.asmt_list['handle'])
            fun.open_gl_create_page(self.driver, "group")
            gp_asmt_config_page = GPAsmtConfigPage(self.driver)
            self.__fill_gp_asmt_form(gp_asmt_config_page, asmt_data)

    def __get_asmt_list_info(self):
        """Only can be used after enter course."""
        for handle in self.driver.window_handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to_window(handle)
                time.sleep(5)
                return {'handle': handle, 'url': self.driver.current_url}

    def __fill_gp_asmt_form(self, page, asmt_data):
        """Config the new group assignments."""
        name_input = page.input_asmt_name(asmt_data[u"name_input"])
        due_date = page.select_due_date()
        page.select_grade_type("Five Star")
        page.show_advanced()
        page.input_instruction()
        page.select_group_formeds("System Formed")
        page.select_peer_review()
        redirct_page = page.save_asmt()
        self.assertEqual(
            redirct_page,
            self.asmt_list['url'],
            msg='Fail to save assignment. {0}, {1}'.
                format(redirct_page, self.asmt_list['url']))
        return {'gp_name': name_input, 'due_date': due_date}
