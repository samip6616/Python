import pandas as pd

s = pd.Series([10,20,30], index=["A","B","C"])

s["D"] = 40

print(s)
