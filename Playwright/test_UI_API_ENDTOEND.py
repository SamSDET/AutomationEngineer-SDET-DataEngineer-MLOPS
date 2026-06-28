from playwright.sync_api import Playwright, expect

from Playwright.Utilities.APIBase import APIUtils

def test_e2e_API_UI(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Create Order
    apiUtils = APIUtils()
    order_ID = apiUtils.createorder(playwright)

    #Login
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    page.locator("#userEmail").fill("abdulsamad453@outlook.com")
    page.get_by_placeholder("enter your passsword").fill("!Jun26@honWRV")
    page.locator("#login").click()
    #input("Enter to close browser")
    #browser.close()
    #page.pause()

    #Order_History
    page.locator("[routerlink='/dashboard/myorders']").click()
    row = page.locator("tr").filter(has_text=order_ID)
    row.get_by_role("button", name="View").click()
    try:
        expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
        print("Test Passed")
    except:
        print("Test Failed")
        page.pause()
        
    
   

