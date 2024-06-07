'''This code is to get all the url present from page 1 of a website to the mentioned page number
You will have to provide the base url without the page number 
and through inspect element find out the common class name where the links that you want are present'''

from playwright.sync_api import sync_playwright
import sys

def run(playwright):
    browser = playwright.chromium.launch(headless=True) 
    context = browser.new_context()  
    page = context.new_page()  

    
    #base_url = "https://scholar.google.com/scholar?q=sleep+inertia&hl=en&as_sdt=0,5&start="
    base_url = "https://scholar.google.com/scholar?q=coffee&hl=en&as_sdt=0,5&start="

    for i in range(0, 1000, 10):  # 0 to 90
        url = f"{base_url}{i}"  # Construct the URL for the current page
        page.goto(url)  
        
        # Wait for the necessary elements to load
        page.wait_for_selector(".gs_ri")
        
        # Extract the information
        results = page.query_selector_all(".gs_ri") 
        for result in results:
            title_element = result.query_selector("h3.gs_rt") #the common class name of the link
            title = title_element.text_content().strip()
            link_element = title_element.query_selector("a")
            link = link_element.get_attribute("href") if link_element else "No link available"
            print(f"Title: {title}\nLink: {link}\n")
    
    
    browser.close()

# Ensure the script prints to the console using UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as playwright:
    run(playwright)
