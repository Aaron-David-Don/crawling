'''this code convert the webisite to markdown format(only 1 page)'''
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="use ur api key")


crawl_result = app.crawl_url('https://www.ncbs.res.in/', {'crawlerOptions': {'excludes': []}})

# Get the markdown for each crawled page
for result in crawl_result:
    print(result['markdown'])
