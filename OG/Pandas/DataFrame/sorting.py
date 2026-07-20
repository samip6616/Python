import pandas as pd

student = {
    "Name": ["Ram", "Hari", "Sita", "Gita", "Nikita", "Divine", "Sajan", "Kashmira"],
    "Age": [20, 21, 19, 22, 27, 24, 23, 26],
    "Marks": [85, 90, 95, 88, 86, 84, 83, 81]
}

df = pd.DataFrame(student)

#Sorting Data
#Sort by Column
print(df.sort_values(by="Marks"))
#Sort by Index
print(df.sort_index())
