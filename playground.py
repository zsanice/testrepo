import pandas as pd

# Define the file path
file_path = "/Users/mela/Projects/Data/pullrequests/data.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Replace missing values with '--'
df.fillna('--', inplace=True)

# Print the first 5 rows with headers
print(df.head(5))

import matplotlib.pyplot as plt