import re
from urllib.parse import urljoin

def extract_urls(markdown_content, base_url):
    url_pattern = re.compile(r'\[.*?\]\((.*?)\)')
    
    # Find all matches
    matches = url_pattern.findall(markdown_content)
    for match in matches:
        # If the URL is partial, join it with the base URL
        complete_url = urljoin(base_url, match)
        print(f"{complete_url}")

with open('output\page_2.md', 'r') as file:
    markdown_content = file.read()

base_url = 'https://pubmed.ncbi.nlm.nih.gov'
extract_urls(markdown_content, base_url)
