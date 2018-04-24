"""
Test teacher create different assignments.

  includes: gp, ip, qa
"""
from models.TeacherTest import TeacherTest
from page_obj.AsmtConfigPage import AsmtConfigPage
import models.function as fun


class CreateAsmtTest(TeacherTest):
    """Create assignments test."""

    def test_gp_asmt_create(self):
        """Test create new group assignments."""
        title = fun.enter_course(self.driver, "bigbengenerallink")
        self.assertEqual(
            title,
            "bigbengenerallink: videoassignments"
        )
        self.driver.asmt_list_url = fun.switch_to_asmt(self.driver)
        fun.open_gl_create_page(self.driver, "group")
        asmt_config_page = AsmtConfigPage(self.driver)
        self.fill_gp_asmt_form(asmt_config_page)

    def fill_gp_asmt_form(self, page):
        """Config the new group assignments."""
        name_input = page.input_asmt_name("_Ren_GP")
        due_date = page.select_due_date()
        page.select_grade_type("Five Star")
        """
        show_advanced(self.driver)
        instruction(self.driver)
        group_formeds(self.driver, "System Formed")
        peer_review(self.driver)
        save_asmt(self.driver, name_input, driver.asmt_list_url)
        return {'gp_name': name_input, 'due_date': due_date }
        """
