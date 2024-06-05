import os
from firecrawl import FirecrawlApp

with open('output\pubmed_url.txt', 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

api_keys = [
    "fc-4d24b3ac55724dadabcdf816551b2c46",
    "fc-33b4ec3c4b5a4e7fa5b40a66d95340cd",
    "fc-1234567890abcdef1234567890abcdef",
]

api_key_index = 0

def get_firecrawl_app():
    return FirecrawlApp(api_key=api_keys[api_key_index])

output_dir = "output_ncs"
os.makedirs(output_dir, exist_ok=True)

for i, url in enumerate(urls, start=1):
    while True:
        try:
            firecrawl = get_firecrawl_app()
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
            break  # Exit the while loop if successful
        except Exception as e:
            error_message = str(e)
            print(f"Error scraping {url}: {error_message}")
            if "Status code: 429" in error_message:
                api_key_index = (api_key_index + 1) % len(api_keys)
                print(f"Switching API key to: {api_keys[api_key_index]}")
            else:
                break  # Skip the current URL and proceed to the next one
