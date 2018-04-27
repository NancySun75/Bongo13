"""Functions."""
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def login_bigben(driver, user_name, user_pwd):
    """Login bigben."""
    home_cur_url = "https://bigben-moodle.youseeu.com"
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
        "[aria-label='Add New Item']"
    )
    add_new_item.click()

    # local 3 project icon
    project_dics = {
        "question_answer":
            "[aria-label='Create question & answer assignment']",
        "group":
            "[aria-label='Create group assignment']",
        "individual":
            "[aria-label='Create individual assignment']"
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
