import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(buttons) == 1, "Do not find basket button!"
    time.sleep(5)
