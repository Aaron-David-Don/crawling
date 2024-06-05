import os
from firecrawl import FirecrawlApp

# Define the URLs to crawl
urls = [
    "https://pubmed.ncbi.nlm.nih.gov/?term=sleep%20inertia&size=200&page=1",
    "https://pubmed.ncbi.nlm.nih.gov/?term=sleep%20inertia&size=200&page=2"
]

# Initialize FirecrawlApp with the API key
firecrawl = FirecrawlApp(
    api_key="fc-33b4ec3c4b5a4e7fa5b40a66d95340cd",
)

# Create the output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Iterate over each URL and perform the crawl
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

    # Save the result as a markdown file
    if 'markdown' in page_content:
        markdown_content = page_content['markdown']
        file_path = os.path.join(output_dir, f"page_{i}.md")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(markdown_content)
        print(f"Saved: {file_path}")
    else:
        print(f"Failed to retrieve content for URL: {url}")
