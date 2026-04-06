from playwright.sync_api import Playwright

def test_e2e_API_UI(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("htps://rahulshettyacademy.com/client/")


    
