'''This code is to scrape given pages of a website using firecrawl api '''
import os
from firecrawl import FirecrawlApp

urls = [
    "https://pubmed.ncbi.nlm.nih.gov/?term=sleep%20inertia&size=200&page=1",
    "https://pubmed.ncbi.nlm.nih.gov/?term=sleep%20inertia&size=200&page=2"
]


firecrawl = FirecrawlApp(
    api_key="haha use ur api key",
)
#create one file
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

for i, url in enumerate(urls, start=1):
    page_content = firecrawl.scrape_url(
        url=url,
        params={
            "pageOptions": {
                "onlyMainContent": True  # Ignore navs, footers, etc.
            },
            "crawlerOptions": {
                "excludes": []
            }
        }
    )

    if 'markdown' in page_content:
        markdown_content = page_content['markdown']
        file_path = os.path.join(output_dir, f"page_{i}.md")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(markdown_content)
        print(f"Saved: {file_path}")
    else:
        print(f"Failed to retrieve content for URL: {url}")
