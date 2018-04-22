"""Functions."""


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
