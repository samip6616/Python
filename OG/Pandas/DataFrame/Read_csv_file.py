import pandas as pd

# Importing Data from CSV
df = pd.read_csv("data.csv")

#Print first 5 rows
print(df.head())

#Print all data
print(df.to_string())
