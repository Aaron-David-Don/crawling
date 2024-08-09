# THIS REPOSITORY IS MAINLY USED FOR CRAWLING AND SCRAPING WEBSITES               
# TO CONVERT WEBSITES TO MARKDOWN FORMAT TO FEED LLMS

1. **basic_scraper.py**
   - This code is used to simply scrape a single website and obtain a markdown data of the website. This is obtained by using playwright API key.
   
2. **extract_url_from_pages-playwright.py**
   - This code is used to scrape specific data from all the page numbers present in the website by providing the unique class id where the data exists in all the pages. Here, this code is to get all the URL present from page 1 of a website to the mentioned page number. You will have to provide the base URL without the page number and through inspect element find out the common class name where the links that you want are present.

3. **extract_googlescholar_with_delay.py**
   - This code is same to extract_url_from_pages-playwright.py but here a time delay has been added as when you try to scrape huge amount of data from google scholar, they'll ban your code to run
on the specific IP address hence a time delay 
that ranges from 3 to 6 seconds has been added.

4. **extract_all_urls-playwright_bfs.py**
   - This code is to all the URL present on the website meaning, it will extract the URL from all `<a href>` tag present on the specific page as well as within the URL extracted extract from the `<a href>` tags. It is done using an algorithm called BFS which stands for Breadth First Search therefore it works in a binary tree format by visiting the home page and extracting all the links then going to the first URL website and extracting all the links once it done with extracting all the URL from the URLs present in the home page it goes to the first URL of the first URL present in home page and so on... In simpler words, it goes level by level similar to a family tree generations.
   
5. **extract_info_from_class-playwright.py**
   - This code is used to extract a specific type of info from websites it uses playwright to look for specific class name and extracts info from that. Here this code is used to extract DOI links from several URLs mentioned in a text file (contains clean URL [code to clean links is also provided below] after extracting from several pages [extract_url_from_pages-playwright.py] or hyperlink [extract_all_urls-playwright_bfs.py] with the help of playwright )
   
6. **cleaning_links-EAUPB.py**
   - This code is to clean the output present in a text file received from extract_all_urls-playwright-bfs.py it provides only the links with no duplicates
   
7. **cleaning_links-EIFCP.py**
   - This code is used to clean links present in text file and upload it in another text file here the obilink.txt (extracted using extract_info_from_class-palywright.py) had other links other than obi so this code removes all the other link
   
8. **join_partial_urls.py**
   - While scraping, certain website contain only partial URL which is an issue therefore this code combines the partial URL with the base URL
   
9. **firecrawl_scrape_pages.py**
   - This code is to scrape given pages of a website using firecrawl API note- this code can cause 421 rapid rate issue and wont let user to scrape multiple site It can be fixed using the given .py code below
   
10. **premium_firecrawl.py**
   - This code breaks the firecrawl 429 rapid rate issue as it wont let user scrape multiple websites Hence with this code you can scrape how much ever you want provided there is all the URL provided in a text file this can be achieved using either of my code- extract_all_urls-playwright_bfs.py or extract_url_from_pages-playwright.py
   
11. **scihub_download.py**
    - This code is to download all the DOI files from SCIHUB given a text file having all the DOI link

12. **web_content.js**
    - This code is to extract only the text content of a website
      
13. **select.js**
    - This code is to extract the selected text from the website by the user
      
14. **LlmSanksrit.py**
    - With help of ollama replicate and translate building a sanksrit chatbot
