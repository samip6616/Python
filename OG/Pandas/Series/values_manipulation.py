import pandas as pd

s = pd.Series([10,20,30], index=["A","B","C"])

#Add New Value
s["D"] = 40

print(s)

#Updating Values
s["B"] = 50

print(s)

#Deleting Elements
s = s.drop("C")

print(s)

#Filtering Data
series = pd.Series([10,20,30,40,50])

print(series[series > 25])
