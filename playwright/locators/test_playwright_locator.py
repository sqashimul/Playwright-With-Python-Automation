import time
import re
from playwright.sync_api import Page, expect

# Method Name
# 1) page.get_by_alt_text
# 2) page.get_by_text()

def test_text_verify_playwright_locators(page: Page):
    page.goto("https://www.daraz.com.bd/", wait_until="domcontentloaded", timeout=60000)
    # page.goto("https://www.daraz.com.bd/", wait_until="domcontentloaded")
    time.sleep(5)  # seconds
    page.wait_for_timeout(10000)  # 5000 ms = 5 sec
    # 1) page.get_by_alt_text
    logo = page.get_by_alt_text("Online Shopping Daraz Logo")
    expect(logo).to_be_visible()

    # 2) page.get_by_text()
    expect(page.get_by_text("Flash Sale")).to_be_visible() # full text
    expect(page.get_by_text("Flash ")).to_be_visible() # partial text
    expect(page.get_by_text(re.compile(".*Flash.*"))).to_be_visible() # regular expression

# --headed -- More Run Debug -- Modify Run Configuration --
# Terminal Run Configuration
# pytest -v -s --headed --browser chromium
# pytest playwright/locators/test_playwright_locator.py -s -v --headed

