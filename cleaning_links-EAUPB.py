'''This code is to clean the output received from 
extract_all_urls-playwright-bfs.py
It provides only the links with no duplicates'''
import re

def extract_urls(input_file, output_file):
    # Regular expression for matching URLs
    url_pattern = re.compile(r'(https?://[^\s]+)')
    
    
    urls = set()
    
    with open(input_file, 'r') as file:
        for line in file:
            matches = url_pattern.findall(line)
            for match in matches:
                # Remove URLs ending with a comma or colon
                if not (match.endswith(',') or match.endswith(':')):
                    urls.add(match)
    
    
    with open(output_file, 'w') as file:
        for url in sorted(urls):
            file.write(url + '\n')


input_file = 'output\page_1.md'
output_file = 'output\outputpg1.txt'
extract_urls(input_file, output_file)
