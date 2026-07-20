import pandas as pd

#1. From a Dictionary
data1 = {
    "Name": ["Ram", "Hari", "Sita"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 95]
}

df = pd.DataFrame(data1)

print(df)

#2. From a List of Lists
data2 = [
    ["Ram", 20, 85],
    ["Hari", 21, 90],
    ["Sita", 19, 95]
]

df = pd.DataFrame(data2, columns=["Name", "Age", "Marks"])

print(df)

#3. From a List of Dictionaries
data3 = [
    {"Name": "Ram", "Age": 20},
    {"Name": "Hari", "Age": 21},
    {"Name": "Sita", "Age": 19}
]

df = pd.DataFrame(data3)

print(df)
