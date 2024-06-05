import time
from scidownl import scihub_download

def download_one_paper():
    """Example of downloading one paper.
    The paper will be downloaded the ./paper/ directory, and
    the filename is one_paper.pdf
    """
    paper = "https://doi.org/10.1145/3375633"
    paper_type = "doi"
    out = "./paper/one_paper.pdf"
    scihub_download(paper, paper_type=paper_type, out=out)

def download_multi_papers(url_file):
    """Example of downloading multiple papers.
    All papers will be downloaded to the ./paper/ directory,
    and their filenames are the paper titles.
    The URLs will be read from a provided text file.
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
    url_file = 'output\obilinkclean.txt'  # The text file containing the URLs
    download_multi_papers(url_file)
