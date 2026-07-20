import pandas as pd
import numpy as np

#Handling Missing Values

data = {
    "Name": ["Ram", "Hari", "Sita"],
    "Marks": [85, np.nan, 95]
}

df = pd.DataFrame(data)

print(df.isnull())

#Filling Missing Values
df["Marks"] = df["Marks"].fillna(0)

print(df)

#Removing Missing Values
df = df.dropna()

print(df)
