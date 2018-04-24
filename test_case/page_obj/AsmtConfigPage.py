"""Assignment config page."""
import time


class AsmtConfigPage():
    """Assignment config page object."""

    def __init__(self, driver):
        """Init method to prepare browser driver."""
        self.driver = driver

    def input_asmt_name(self, custumer_pattern):
        """Input Assignment name."""
        lt = time.localtime()
        date_str = time.strftime("%m%d%H%M", lt)
        name_input = date_str + custumer_pattern
        assignment_name = self.driver.find_element_by_id(
            "activity-name-textfield"
        )
        assignment_name.send_keys(name_input)
        return name_input

    def select_due_date(self):
        """Select due date and due time."""
        due_date = self.driver.find_element_by_id("due-date-datepicker")
        due_date.click()
        # make sure date by calander
        lt = time.localtime()
        day_str = time.strftime("%d", lt)
        day_num = int(day_str)
        day_args = self.driver.find_elements_by_css_selector(
            "button.md-calendar-date"
        )
        day_args[day_num].click()
        ok_btn = self.driver.find_elements_by_css_selector(
            "button.md-ink--primary"
        )[1]
        ok_btn.click()
        date_show = due_date.get_attribute("value")
        return date_show

    def select_grade_type(self, grade_type):
        """Select the grade type."""
        grade_type_toggle = self.driver.find_element_by_id("grade-type-toggle")
        grade_type_toggle.click()
        grade_type_dics = {
            "Percentage": "[data-id = '0']",
            "Rubric": "[data-id = '1']",
            "Pass/Fail": "[data-id = '2']",
            "Auto Pass": "[data-id = '3']",
            "Five Star": "[data-id = '4']",
        }
        grade_type_select = self.driver.find_element_by_css_selector(
            grade_type_dics[grade_type]
        )
        grade_type_select.click()
        if grade_type == "Rubric":
            self.select_rubric(self.driver, "examplerubric.csv")

    def select_rubric(self, rubric_name):
        """Select rubric."""
        rubric_toggle = self.driver.find_element_by_css_selector(
            '[aria-label="Rubric"]'
        )
        rubric_toggle.click()

        rubric_list_items = self.driver.find_elements_by_css_selector(
            "#rubric-menu-options .md-list-item .md-tile-content")
        for i in rubric_list_items:
            if rubric_name == i.text:
                i.click()
                break
