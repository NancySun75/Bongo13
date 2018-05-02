"""
Test teacher create different assignments.

  includes: gp, ip, qa
"""
from models.TeacherTest import TeacherTest
from models.DDT import DDT
from page_obj.GPAsmtConfigPage import GPAsmtConfigPage
from page_obj.IPAsmtConfigPage import IPAsmtConfigPage
from page_obj.QAAsmtConfigPage import QAAsmtConfigPage
import models.function as fun
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


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
            fun.open_asmt_create_page(self.driver, "group")
            gp_asmt_config_page = GPAsmtConfigPage(self.driver)
            self.__fill_gp_asmt_form(gp_asmt_config_page, asmt_data)

    def test_ip_asmt_create(self):
        """Test create new individual assignments."""
        self.data = DDT('data/ip_asmt_create.xlsx').get_data_from_file()
        title = fun.enter_course(self.driver, "bigbengenerallink")
        self.asmt_list = self.__get_asmt_list_info()
        self.assertEqual(
            title,
            "bigbengenerallink: videoassignments"
        )

        for asmt_data in self.data:
            fun.switch_to_asmt(self.driver, self.asmt_list['handle'])
            fun.open_asmt_create_page(self.driver, "individual")
            ip_asmt_config_page = IPAsmtConfigPage(self.driver)
            self.__fill_ip_asmt_form(ip_asmt_config_page, asmt_data)

    def test_qa_asmt_create(self):
        """Test create new qa assignments."""
        self.data = DDT('data/qa_asmt_create.xlsx').get_data_from_file()
        title = fun.enter_course(self.driver, "bigbengenerallink")
        self.asmt_list = self.__get_asmt_list_info()
        self.assertEqual(
            title,
            "bigbengenerallink: videoassignments"
        )

        for asmt_data in self.data:
            fun.switch_to_asmt(self.driver, self.asmt_list['handle'])
            fun.open_asmt_create_page(self.driver, "question_answer")
            qa_asmt_config_page = QAAsmtConfigPage(self.driver)
            self.__fill_qa_asmt_form(qa_asmt_config_page, asmt_data)

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

    def __fill_gp_asmt_form(self, page, asmt_data):
        """Config the new group assignments."""
        page.input_asmt_name(asmt_data[u"name_input"])
        page.select_due_date()
        page.select_grade_type(asmt_data[u"grade_type"])
        page.show_advanced()
        page.input_instruction(
            asmt_data[u"instructions"],
            asmt_data[u"post_sub_instructions"]
        )
        page.select_group_formeds(asmt_data[u"group_formed"])
        page.select_peer_review()
        redirct_page = page.save_asmt()
        self.assertEqual(
            redirct_page,
            self.asmt_list['url'],
            msg='Fail to save assignment. {0}, {1}'.
                format(redirct_page, self.asmt_list['url']))

    def __fill_ip_asmt_form(self, page, asmt_data):
        """Config the new individual assignments."""
        page.input_asmt_name(asmt_data[u"name_input"])
        page.select_due_date()
        page.select_grade_type("Pass/Fail")
        page.show_advanced()
        page.input_instruction()
        redirct_page = page.save_asmt()
        self.assertEqual(
            redirct_page,
            self.asmt_list['url'],
            msg='Fail to save assignment. {0}, {1}'.
                format(redirct_page, self.asmt_list['url']))

    def __fill_qa_asmt_form(self, page, asmt_data):
        """Config the new individual assignments."""
        page.input_asmt_name(asmt_data[u"name_input"])
        page.select_due_date()
        page.select_grade_type("Pass/Fail")
        page.show_advanced()
        page.input_instruction()
        page.add_questions(2)
        page.select_peer_review()
        redirct_page = page.save_asmt()
        self.assertEqual(
            redirct_page,
            self.asmt_list['url'],
            msg='Fail to save assignment. {0}, {1}'.
                format(redirct_page, self.asmt_list['url']))
