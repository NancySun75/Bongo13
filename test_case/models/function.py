"""Functions."""
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


def login_bigben(driver, user_name, user_pwd):
    """Login bigben."""
    home_cur_url = "https://bongo13-moodle.youseeu.com/"
    driver.get(home_cur_url)
    user_login(driver, user_name, user_pwd)


def user_login(driver, user_name, user_pwd):
    """Login from login page by user_name."""
    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys(user_name)  # input educator-1 as username
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys(user_pwd)
    driver.find_element_by_css_selector('[type="submit"]').click()


def open_asmt_create_page(driver, project_type):
    """
    Create new assignment by teacher.

    Support 'question_answer', 'group' and 'individual' types.
    """
    add_new_item = driver.find_element_by_css_selector(
        ".speed-dial-button"
    )
    add_new_item.click()

    # local 4 project icon
    project_dics = {
        "question_answer":
            "[aria-label='Create question & answer assignment']",
        "group":
            "[aria-label='Create group assignment']",
        "individual":
            "[aria-label='Create individual assignment']",
        "interactive":
            "[aria-label='Create interactive video assignment']"
    }

    project_type_icon = driver.find_element_by_css_selector(
        project_dics[project_type]
    )
    ActionChains(driver).move_to_element(
        project_type_icon
    ).perform()
    project_type_icon.click()


def enter_course(driver, link):
    """Click a link to enter corresponding course."""
    class_link = driver.find_element_by_link_text(link)
    class_link.click()
    time.sleep(5)
    return driver.title


def switch_to_asmt(driver, handle):
    """Switch to assignment list iframe."""
    driver.switch_to_window(handle)
    condition = expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, ".content-title-header")
    )
    WebDriverWait(driver, 60, 0.5).until(condition)


def found_asmt_by_page(driver, asmt_name):
    """Use with found_asmt and open_asmt functions as a student."""
    found = found_asmt(driver, asmt_name)
    while found is False:
        next_page = driver.find_element_by_css_selector(
            "#data-table-pagination-increment-btn"
        )
        next_page.click()
        found = found_asmt(driver, asmt_name)


def found_asmt(driver, asmt_name):
    """Found asmt in one page as a student."""
    rows = driver.find_elements_by_css_selector(
        '[aria-label="Open assignment"]')
    for row in rows:
        name = row.text
        if asmt_name == name:
            open_asmt(driver, row)
            return True
    return False


def open_asmt(driver, row):
    """Click and open this asmt page."""
    row.click()


def delete_asmt(driver, handle, asmt_name):
    """Delete the found assignment from pages."""
    switch_to_asmt(driver, handle)
    found = found_delete_asmt(driver, asmt_name)
    while found is False:
        next_page = driver.find_element_by_css_selector(
            "#data-table-pagination-increment-btn"
        )
        next_page.click()
        found = found_delete_asmt(driver, asmt_name)


def found_delete_asmt(driver, asmt_name):
    """Found the assignment to be delete from one page."""
    rows = driver.find_elements_by_css_selector(".md-table-row")
    for row in rows:
        name = row.find_element_by_css_selector("span").text
        if asmt_name == name:
            three_point = row.find_element_by_css_selector(
                '[aria-label="Additional Options"]'
            )
            three_point.click()

            delete_icon = driver.find_element_by_css_selector(
                '[aria-label = "Delete, icon"]'
            )
            ActionChains(driver).move_to_element(delete_icon).perform()
            time.sleep(1)
            delete_icon.click()

            try:
                yes_btn = driver.find_element_by_css_selector(
                    '[aria-label="Yes"]'
                )
                yes_btn.click()
            except NoSuchElementException:
                row.click()
            time.sleep(1)
            return True
    return False
