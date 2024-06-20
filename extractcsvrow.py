import pandas as pd

# Load the CSV file
file_path = '/Users/ayushyadav/Documents/GitHub/crawling/compro_json2csv.csv'
data = pd.read_csv(file_path)

# Extract the third column
third_column = data.iloc[:, 2]

# Save the third column to a new file
output_path = './third_column.csv'
third_column.to_csv(output_path, index=False)


