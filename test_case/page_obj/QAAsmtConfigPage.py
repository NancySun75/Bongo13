"""Assignment config page."""
import time
import random


class QAAsmtConfigPage():
    """Assignment config page object."""

    def __init__(self, driver):
        """Init method to prepare browser driver."""
        self.driver = driver

    def input_asmt_name(self, name_input):
        """Input Assignment name."""
        asmt_name = self.driver.find_element_by_id(
            "activity-name-textfield"
        )
        asmt_name.send_keys(name_input)
        return name_input

    def select_due_date(self):
        """Select due date and due time."""
        due_date = self.driver.find_element_by_id("due-date-datepicker")
        due_date.click()
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
        time.sleep(1)
        return date_show

    def select_grade_type(self, grade_type):
        """Select the grade type."""
        grade_type_toggle = self.driver.find_element_by_id(
            "grade-type-toggle"
        )
        grade_type_toggle.click()
        time.sleep(1)
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
            "#rubric-menu-options .md-list-item .md-tile-content"
        )
        for i in rubric_list_items:
            if rubric_name == i.text:
                i.click()
                break

    def show_advanced(self):
        """Advanced show."""
        show_advance = self.driver.find_element_by_css_selector(
            "[aria-label='Show Advanced']"
        )
        show_advance.click()

    def input_instruction(self):
        """Input instructions and post submission instructions."""
        e_ins = self.driver.find_element_by_css_selector(
            "#instructions-textfield"
        )
        ins = "This message is testing instructions text."
        e_ins.send_keys(ins)

        e_ins_post = self.driver.find_element_by_css_selector(
            "#post-submission-instructions-textfield"
        )
        ins_post = "This message is post submission instructions text."
        e_ins_post.send_keys(ins_post)
        return {'ins_text': ins, 'post_ins_text': ins_post}

    def add_questions(self, question_number):
        """Add question by specific number."""
        print "-----------"
        for i in range(0, question_number):
            add_question = self.driver.find_element_by_css_selector(
                "[aria-label='Add Question']"
            )
            add_question.click()
            question_text = self.driver.find_element_by_css_selector(
                '#question-text' + i
            )
            question_content = "This is the %dth question test." % i
            question_text.send_keys(question_content)

    def select_recording_option(self):
        """Select recording option."""
        random_qestion_num = self.driver.find_element_by_css_selector(
            "#amount_of_random_questions"
        )
        random_qestion_num.send_keys(random.randint(1, 2))

    def select_peer_review(self):
        """
        Peer Review.

        (allow_peer_review_before_sbmt:aprbs) (anonymous_peer_comments: apc).
        """
        num_of_rr = random.randint(0, 3)
        peer_review_amount = self.driver.find_element_by_css_selector(
            "#peer_review_amount"
        )
        peer_review_amount.clear()
        peer_review_amount.send_keys(num_of_rr)
        time.sleep(3)

    def save_asmt(self):
        """Save assignment."""
        show_advance = self.driver.find_element_by_css_selector(
            "[aria-label='Save']"
        )
        show_advance.click()
        time.sleep(10)
        return self.driver.current_url
