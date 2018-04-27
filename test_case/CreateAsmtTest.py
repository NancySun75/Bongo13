"""
Test teacher create different assignments.

  includes: gp, ip, qa
"""
from models.TeacherTest import TeacherTest
from models.DDT import DDT
from page_obj.GPAsmtConfigPage import GPAsmtConfigPage
import models.function as fun


class CreateAsmtTest(TeacherTest):
    """Create assignments test."""

    def test_gp_asmt_create(self):
        """Test create new group assignments."""
        self.data = DDT('data/gp_asmt_create.xlsx').get_data_from_file()
        title = fun.enter_course(self.driver, "bigbengenerallink")
        self.home_handle = self.driver.current_window_handle
        self.assertEqual(
            title,
            "bigbengenerallink: videoassignments"
        )

        for asmt_data in self.data:
            self.asmt_list_url = fun.\
                switch_to_asmt(self.driver, self.home_handle)
            fun.open_gl_create_page(self.driver, "group")
            gp_asmt_config_page = GPAsmtConfigPage(self.driver)
            self.fill_gp_asmt_form(gp_asmt_config_page, asmt_data)

    def fill_gp_asmt_form(self, page, asmt_data):
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
            self.asmt_list_url,
            msg="Fail to save assignment.")
        return {'gp_name': name_input, 'due_date': due_date}
