from playwright.sync_api import sync_playwright

def apply_job(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url)

        print("Opened:", url)

        # Demo fill
        try:
            page.fill("input[name='name']", "Rushikesh")
            page.fill("input[type='email']", "test@email.com")
        except:
            print("Fields not found (ATS dynamic)")

        browser.close()