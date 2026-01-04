from playwright.sync_api import Page, expect
import time
def test_UIChecks(playwright):
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context()
    driver = context1.new_page()
    driver.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(driver.get_by_placeholder("Hide/Show Example")).to_be_visible()
    driver.get_by_role("button",name="Hide").click()
    expect(driver.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)
    def handle_popup(popup):
        assert popup.message == "Hello , Are you sure you want to confirm?"
        popup.accept()
    driver.on("dialog", handle_popup)
    driver.get_by_role("button",name="Confirm").click()
    time.sleep(5)

    driver.locator("#mousehover").hover()
    time.sleep(30)
    driver.get_by_role("link",name="Top").click()

    framedriver = driver.frame_locator("#courses-iframe")
    framedriver.get_by_role("link", name = "All Access plan").click()
    expect(framedriver.locator("body")).to_contain_text(" Happy Subscibers!")


