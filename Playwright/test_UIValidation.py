from playwright.sync_api import Page, expect
import time

def test_UIValidationDynamicScript(playwright):
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context()
    page =context1.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    NokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    NokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)

def test_child_parent_example(playwright):
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context()
    driver =context1.new_page()
    driver.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    with driver.expect_popup() as child_page:
        driver.locator(".blinkingText").click()
    child_driver = child_page.value
    text1 = child_driver.locator(".red").text_content()
    print(text1)
    words = text1.split("at")
    print(words[1])
    print(words[0])
    email = words[1].strip().split(" ")
    print(email[0])
    assert email[0] == "mentor@rahulshettyacademy.com"
    
