from playwright.sync_api import sync_playwright
import sys
import time
import random
from datetime import datetime
import csv

def run(playwright):
    browser = playwright.chromium.launch(headless=True) 
    context = browser.new_context()  
    page = context.new_page()  

    base_url = ""

    # Get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open the CSV file in append mode
    with open("googlescrape.csv", "a", newline='', encoding="utf-8") as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)
        
        # Write the header if the file is empty
        csvfile.seek(0, 2)  # Move the cursor to the end of the file
        if csvfile.tell() == 0:  # Check if the file is empty
            csvwriter.writerow(["Index", "Timestamp", "Title", "URL"])
        
        index = 964
        for i in range(964, 1000, 10):  # 0 to 90
            url = f"{base_url}{i}"  # Construct the URL for the current page
            page.goto(url)  
            
            # Wait for the necessary elements to load
            page.wait_for_selector(".gs_ri")
            
            # Extract the information
            results = page.query_selector_all(".gs_ri") 
            for result in results:
                title_element = result.query_selector("h3.gs_rt")  # the common class name of the link
                title = title_element.text_content().strip()
                link_element = title_element.query_selector("a")
                link = link_element.get_attribute("href") if link_element else "No link available"
                
                # Write the result to the CSV file
                csvwriter.writerow([index, current_time, title, link])
                
                index += 1


        
    browser.close()

# Ensure the script prints to the console using UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as playwright:
    run(playwright)