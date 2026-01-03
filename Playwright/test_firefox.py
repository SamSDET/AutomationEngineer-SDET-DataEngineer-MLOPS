import time
from playwright.sync_api import Page, expect
def test_playwright_function(playwright):
    browser = playwright.firefox.launch(headless=False)
    context1 = browser.new_context()
    page1 =context1.new_page()
    page1.goto("https://rahulshettyacademy.com")

def test_another_function(page1:Page):
    page1.goto("https://rahulshettyacademy.com")

def test_corelocators(playwright):
    browser = playwright.firefox.launch(headless=False)
    context1 = browser.new_context()
    page1 =context1.new_page()
    page1.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page1.get_by_label("Username:").fill("rahulshettyacademy")
    page1.get_by_label("Password:").fill("learning1")
    page1.get_by_role("combobox").select_option("teach")
    page1.locator("#terms").check()
    #time.sleep(5)
    page1.get_by_role("link", name="terms and conditions").click()
    #id it becomes CSS .classname becomes CSS
    page1.locator("#signInBtn").click()
    expect(page1.get_by_text("Incorrect username/password.")).to_be_visible()

