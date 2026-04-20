from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.redbus.in")

    page.wait_for_load_state("networkidle")

    cookies = context.cookies()
    print("Cookies:", cookies)

    with open("red_bus_cookies.json", "w") as f:
        json.dump(cookies, f, indent=4)

    with open("red_bus_cookies.json", "r") as f:
        cookies = json.load(f)

    context.add_cookies(cookies)

    page.reload()

    print("Cookies applied after reload")

    browser.close()
