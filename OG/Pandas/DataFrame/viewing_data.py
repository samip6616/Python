import pandas as pd

student = {
    "Name": ["Ram", "Hari", "Sita", "Gita", "Nikita", "Divine", "Sajan", "Kashmira"],
    "Age": [20, 21, 19, 22, 27, 24, 23, 26],
    "Marks": [85, 90, 95, 88, 86, 84, 83, 81]
}

df = pd.DataFrame(student)

print(df.head())      # First 5 rows
print(df.tail())      # Last 5 rows
print(df.sample(2))   # Random 2 rows
