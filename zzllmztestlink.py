import re

def extract_urls(input_file, output_file):
    # Regular expression for matching URLs
    url_pattern = re.compile(r'(https?://[^\s]+)')
    
    # Set to store unique URLs
    urls = set()
    
    # Read the input file and extract URLs
    with open(input_file, 'r') as file:
        for line in file:
            matches = url_pattern.findall(line)
            for match in matches:
                # Remove URLs ending with a comma or colon
                if not (match.endswith(',') or match.endswith(':')):
                    urls.add(match)
    
    # Write the unique URLs to the output file
    with open(output_file, 'w') as file:
        for url in sorted(urls):
            file.write(url + '\n')

# Example usage
input_file = 'output\page_1.md'
output_file = 'output\outputpg1.txt'
extract_urls(input_file, output_file)
