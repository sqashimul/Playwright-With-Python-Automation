import time

from playwright.sync_api import Page, expect


# page.get_by_alt_text
# def test_text_verify_playwright_locators(page: Page):
#     page.goto("https://www.saucedemo.com/")
#     time.sleep(5) #seconds
#     page.wait_for_timeout(5000)  # 5000 ms = 5 sec
#
#     logo = page.locator(".login_logo")
#     expect(logo).to_be_visible()
#     # expect(page.locator("login_logo")).to_be_visible()
#     username = page.get_by_placeholder("Username")
#     expect(username).to_be_visible()
#
#     password = page.get_by_placeholder("Password")
#     expect(password).to_be_visible()
#
#     login_button = page.get_by_role("button", name="Login")
#     expect(login_button).to_be_visible()

# --headed -- More Run Debug -- Modify Run Configuration --
# Terminal Run Configuration
# pytest -v -s --headed --browser chromium
# pytest playwright/locators/test_playwright_locator.py -s -v --headed

def test_text_verify_playwright_locators(page: Page):
    page.goto("https://www.daraz.com.bd/", wait_until="domcontentloaded", timeout=60000)
    # page.goto("https://www.daraz.com.bd/", wait_until="domcontentloaded")
    time.sleep(5)  # seconds
    page.wait_for_timeout(10000)  # 5000 ms = 5 sec

    logo = page.get_by_alt_text("Online Shopping Daraz Logo")
    expect(logo).to_be_visible()
