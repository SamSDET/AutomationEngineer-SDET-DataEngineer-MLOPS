from playwright.sync_api import Playwright
from Utilities.APIBase import APIUtils 
from playwright.sync_api import expect

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a412bc4378febeacdd5b7e3")

def test_network_2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    driver1 = context.new_page()
    driver1.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    driver1.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    driver1.locator("#userEmail").fill("abdulsamad453@outlook.com")
    driver1.get_by_placeholder("enter your passsword").fill("!Jun26@honWRV")
    driver1.locator("#login").click()
    driver1.locator("button[routerlink='/dashboard/myorders']").click()
    driver1.get_by_role("button", name="View").first.click()
    message = driver1.locator(".blink_me").text_content()
    print(message,":: Test Passed")
    if message == "You are not authorize to view this order":
        driver1.pause()
    else:
        print("Test failed: Expected message not found")
    #abdulwaheed1234@gmail.com/Samadtest123

def test_session_storage(playwright: Playwright):
    session = APIUtils()
    tokenSam = session.getToken(playwright)
    browser =playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{tokenSam}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("button[routerlink='/dashboard/myorders']").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()
    








    
    



    
