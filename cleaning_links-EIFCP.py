'''This code is used to clean links present in text file and upload it in another text file
Here the obilink.txt (extracted using extract_info_from_class-palywright.py) had other links other than obi
so this code removes all the other link'''

def filter_doi_urls(input_file, output_file):
  with open(input_file, "r") as in_file, open(output_file, "w") as out_file:
    for line in in_file:
      url = line.strip()
      if url.startswith("https://doi.org"):
        out_file.write(url + "\n")

if __name__ == "__main__":
  filter_doi_urls("output\obilink.txt", "output\obilinkclean.txt")
  print("Filtered URLs saved to output.txt")
  
