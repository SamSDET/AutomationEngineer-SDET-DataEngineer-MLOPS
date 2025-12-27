import time
from playwright.sync_api import Page
def test_playwright_function(playwright):
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context()
    page =context1.new_page()
    page.goto("https://rahulshettyacademy.com")


def test_another_function(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_corelocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    time.sleep(5)

