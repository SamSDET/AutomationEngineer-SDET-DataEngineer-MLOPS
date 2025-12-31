import time
from playwright.sync_api import Page, expect
def test_playwright_function(playwright):
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context()
    page =context1.new_page()
    page.goto("https://rahulshettyacademy.com")


def test_another_function(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_corelocators(playwright):
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context()
    page =context1.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning1")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    #time.sleep(5)
    #page.get_by_role("link", name="terms and conditions").click()
    #id it becomes CSS .classname becomes CSS
    page.locator("#signInBtn").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

