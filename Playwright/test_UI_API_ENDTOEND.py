from playwright.sync_api import Playwright

def test_e2e_API_UI(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    page.locator("#userEmail").fill("abdulsamad453@outlook.com")
    page.get_by_placeholder("enter your passsword").fill("!Jun26@honWRV")
    page.locator("#login").click()
    
   

