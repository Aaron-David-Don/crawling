#the following code is to get web page content using playwright  
import sys
from playwright.sync_api import sync_playwright

def scrape_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(url)

        content = page.locator('div.slAVV4').all_inner_texts()

        for item in content:
            print(item)

        browser.close()

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.flipkart.com/search?q=Mi%2010000%20mAh%2018%20W%20Power%20Bank&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
scrape_content(url)
