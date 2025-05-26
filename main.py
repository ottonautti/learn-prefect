from playwright.sync_api import sync_playwright
from prefect import flow


@flow(log_prints=True)
def main(url: str = "https://example.com"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        print("Page title:", page.title())
        browser.close()

if __name__ == "__main__":
    main()