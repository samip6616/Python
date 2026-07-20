import pandas as pd

student = {
    "Name": ["Ram", "Hari", "Sita", "Gita", "Nikita", "Divine", "Sajan", "Kashmira"],
    "Age": [20, 21, 19, 22, 27, 24, 23, 26],
    "Marks": [85, 90, 95, 88, 86, 84, 83, 81]
}
df = pd.DataFrame(student)

print(df["Name"]) #Selecting Columns
print(df[["Name", "Marks"]]) #Selecting Multiple Columns

#Using loc (Label-based)
print(df.loc[1]) #Selecting Row by Index Label
print(df.loc[1:4]) #Selecting Multiple Rows by Index Label

#Using iloc (Integer-based)
print(df.iloc[0]) #Selecting Row by Index Position
print(df.iloc[0:3]) #Selecting Multiple Rows by Index Position

print(df.loc[0:1, ["Name", "Marks"]]) #Selecting Specific Rows and Columns
print(df.iloc[0:2, 0:2]) #Selecting Specific Rows and Columns by Position

#Adding New Column
df["Grade"] = ["B", "A", "A", "B", "C", "B", "C", "A"]

print(df)

#Updating Values
df.loc[0, "Marks"] = 88

print(df)

#Deleting Column
df = df.drop("Grade", axis=1)

print(df)

#Deleting Row
df = df.drop(1)

print(df)

#Filtering Data
print(df[df["Marks"] > 85])
