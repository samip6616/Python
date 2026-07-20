import pandas as pd

student = {
    "Name": ["Ram", "Hari", "Sita", "Gita", "Nikita", "Divine", "Sajan", "Kashmira"],
    "Age": [20, 21, 19, 22, 27, 24, 23, 26],
    "Marks": [85, 90, 95, 88, 86, 84, 83, 81]
}

df = pd.DataFrame(student)

#Mathematical Operations
#Aggregate Functions
print(df["Marks"].mean())
print(df["Marks"].sum())
print(df["Marks"].max())
print(df["Marks"].min())

#Descriptive Statistics
print(df.describe())

# Importing Data from CSV
df = pd.read_csv("data.csv")

#Basic Operations
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.max(numeric_only=True))
print(df.min(numeric_only=True))
print(df.count())

#Single Column Operations
print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].max())
print(df["Height"].min())
print(df["Type 2"].count())


group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].max())
print(group["Height"].min())
print(group["Height"].count())
