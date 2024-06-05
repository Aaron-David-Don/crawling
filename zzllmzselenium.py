from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse
from collections import deque

def get_all_urls(base_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        urls = set()
        to_visit = deque([base_url])
        
        while to_visit:
            url = to_visit.popleft()
            if url in urls:
                continue
            urls.add(url)
            
            try:
                page.goto(url, timeout=30000)  # Timeout set to 30 seconds
                page.wait_for_load_state("networkidle")
                
                links = page.locator("a[href]").all()
                for link in links:
                    href = link.get_attribute("href")
                    absolute_url = urljoin(base_url, href)
                    if is_same_domain(base_url, absolute_url) and absolute_url not in urls:
                        to_visit.append(absolute_url)
            except Exception as e:
                print(f"Error visiting {url}: {e}")
        
        browser.close()
        return urls

def is_same_domain(base_url, url):
    return urlparse(base_url).netloc == urlparse(url).netloc

base_url = 'https://pubmed.ncbi.nlm.nih.gov/?term=sleep%20inertia&size=200'
all_urls = get_all_urls(base_url)

for url in all_urls:
    print(url)
