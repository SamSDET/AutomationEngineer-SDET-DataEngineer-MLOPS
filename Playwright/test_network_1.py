from playwright.sync_api import Playwright

irresponsibility = {"data":[], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(json = irresponsibility)

def test_network_1(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    driver1 = context.new_page()
    driver1.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    driver1.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    driver1.locator("#userEmail").fill("abdulsamad453@outlook.com")
    driver1.get_by_placeholder("enter your passsword").fill("!Jun26@honWRV")
    driver1.locator("#login").click()
    driver1.locator("button[routerlink='/dashboard/myorders']").click()
    order_text=driver1.locator(".mt-4").text_content() 
    print(order_text)
    driver1.pause()
