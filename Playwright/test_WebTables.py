from playwright.sync_api import Page, expect
import time
def test_Webtables(playwright):
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context()
    driver = context1.new_page()
    driver.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(driver.locator("th").count()):
        if driver.locator("th").nth(index).filter(has_text="Price").count()>0:
            pricecolValue = index
            print(f"Column index of Price is : {pricecolValue}")
            break
    ricerow = driver.locator("tr").filter(has_text="Rice")   
    expect(ricerow.locator("td").nth(pricecolValue)).to_contain_text("37")
    
    driver.goto("https://rahulshettyacademy.com/AutomationPractice/")
    driver.locator("#mousehover").hover()
    driver.get_by_role("link",name = "Top").click()
    time.sleep(5)

    