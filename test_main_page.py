from selenium.webdriver.common.by import By
from pages.base_page import BasePage

def test_guest_can_go_to_login_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}"
    basePage = BasePage(browser, link)
    basePage.open()
    assert True
