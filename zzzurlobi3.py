from playwright.sync_api import sync_playwright

def extract_links_from_file():
  with open("output\pubmed_url.txt", "r") as file:
    urls = [line.strip() for line in file.readlines()]  
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for url in urls:
      page.goto(url)  
      link_element = page.query_selector('a.id-link')

      if link_element:
        link_href = link_element.get_attribute('href')
        print(link_href)
      else:
        print(f"No element found with class 'id-link' for URL: {url}") 
    browser.close()

if __name__ == "__main__":
  extract_links_from_file()
