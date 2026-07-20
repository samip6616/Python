import pandas as pd

student = {
    "Name": ["Ram", "Hari", "Sita", "Gita", "Nikita", "Divine", "Sajan", "Kashmira"],
    "Age": [20, 21, 19, 22, 27, 24, 23, 26],
    "Marks": [85, 90, 95, 88, 86, 84, 83, 81]
}
df = pd.DataFrame(student)

print(df.shape) #Number of rows and columns
print(df.columns) #Column names
print(df.index) #Row labels
print(df.dtypes) #Data type of each column
print(df.values) #NumPy array of values
print(df.size) #Total number of elements
