"""Assignment config page."""
import time
import random


class GPAsmtConfigPage():
    """Assignment config page object."""

    def __init__(self, driver):
        """Init method to prepare browser driver."""
        self.driver = driver
        self.asmt_name = self.driver.find_element_by_id(
            "activity-name-textfield"
        )
        self.due_date = self.driver.find_element_by_id("due-date-datepicker")

    def input_asmt_name(self, custumer_pattern):
        """Input Assignment name."""
        lt = time.localtime()
        date_str = time.strftime("%m%d%H%M", lt)
        name_input = date_str + custumer_pattern
        self.asmt_name.send_keys(name_input)
        return name_input

    def select_due_date(self):
        """Select due date and due time."""
        self.due_date.click()
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
        date_show = self.due_date.get_attribute("value")
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

    def select_group_formeds(self, group_formed):
        """Select group formed."""
        if group_formed != "Educator Formed":
            group_formation = self.driver.find_element_by_id(
                "executors_type-toggle"
            )
            group_formation.click()
            e_student_formed = self.driver.find_element_by_css_selector(
                "[data-id='1']"
            )
            sf = e_student_formed.find_element_by_css_selector("div").text
            e_system_formed = self.driver.find_element_by_css_selector(
                "[data-id='2']"
            )
            if group_formed == sf:
                e_student_formed.click()
            else:
                e_system_formed.click()
            # Finalize groups at date/time: current_time + after 10mins
            time.sleep(1)
            finalize_date = self.driver.find_element_by_id(
                "finalize-group-date-datepicker"
            )
            finalize_date.click()
            ok_btn1 = self.driver.find_elements_by_css_selector(
                ".md-ink--primary")[1]
            ok_btn1.click()
            time.sleep(1)
            finalize_time = self.driver.find_element_by_id(
                "finalize-group-date-timepicker"
            )
            finalize_time.click()
            ok_btn2 = self.driver.find_elements_by_css_selector(
                ".md-ink--primary")[1]
            ok_btn2.click()
            time.sleep(1)
            max_stn = self.driver.find_element_by_id("max_students_amount")
            max_stn.clear()
            max_stn.send_keys(3)
            time.sleep(1)

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

'''
    def add_questions(self, question_number):
        """Add question by specific number."""
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
'''
