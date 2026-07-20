import pandas as pd

#Sort by Values
s = pd.Series([30,10,40,20])

print(s.sort_values())
'''Output

1    10
3    20
0    30
2    40
dtype: int64
'''
#Sort by Index
series = pd.Series([10,20,30], index=["b","c","a"])

print(series.sort_index())

'''Output

a    30
b    10
c    20
dtype: int64'''
