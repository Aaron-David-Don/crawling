'''This code is to download all the DOI files from SCIHUB
a text file having all the DOI link should be provided  '''
import time
from scidownl import scihub_download

def download_one_paper():
    #downloading one paper.
    paper = "https://doi.org/10.1145/3375633"
    paper_type = "doi"
    out = "./paper/one_paper.pdf"
    scihub_download(paper, paper_type=paper_type, out=out)

def download_multi_papers(url_file):
    """Example of downloading multiple papers.
    All papers will be downloaded paper folder
    and their filenames are the paper titles.
    """
    with open(url_file, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if url:
            if "doi.org" in url:
                paper_type = "doi"
            elif "pubmed.ncbi.nlm.nih.gov" in url or "pmid" in url:
                paper_type = "pmid"
            else:
                paper_type = "title"
            out = "./paper/"
            scihub_download(url, paper_type=paper_type, out=out)
            time.sleep(3.69)  # Adding a delay of 3 seconds after each download

if __name__ == '__main__':
    url_file = "cleaned_dois.csv"
    download_multi_papers(url_file)
