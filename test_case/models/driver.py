from selenium import webdriver  # NOQA
from selenium.webdriver.chrome.options import Options


def chrome():
    """Init chrome driver with a consistent cache config."""
    options = Options()
    options.add_argument("user-data-dir=/tmp/tarun")
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()  # browser full screen
    driver.implicitly_wait(10)
    return driver
