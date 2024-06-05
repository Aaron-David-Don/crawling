from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-33b4ec3c4b5a4e7fa5b40a66d95340cd")

# Crawl a website
crawl_result = app.crawl_url('https://www.ncbs.res.in/', {'crawlerOptions': {'excludes': []}})

# Get the markdown for each crawled page
for result in crawl_result:
    print(result['markdown'])