"""
Test teacher create different assignments.

  includes: gp, ip, qa
"""
from models.TeacherTest import TeacherTest
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
