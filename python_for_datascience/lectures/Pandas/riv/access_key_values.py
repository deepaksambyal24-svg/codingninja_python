import pandas as pd

data = {'Delhi': 31.0, 'Mumbai': 20.0, 'Chennai': 10.5, 'Kolkata': 14.0}
series = pd.Series(data)

# Write your code from here
ind=series.index
print(ind)
val=series.values
print(val)