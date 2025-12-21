from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        print("Launching Chromium browser...", flush=True)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = "https://www.apple.com/in/shop/buy-iphone"
        print(f"Navigating to {url}", flush=True)
        page.goto(url)

        title = page.title()
        print(f"Page title is: {title}", flush=True)

        # Flexible assertion
        assert "iPhone" in title
        print("Assertion passed: 'iPhone' is in the title", flush=True)

        browser.close()
        print("Browser closed successfully", flush=True)