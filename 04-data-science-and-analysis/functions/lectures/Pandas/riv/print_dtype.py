import pandas as pd

data = [10, 20.5, "Python", True, None]
series = pd.Series(data)

# Write your code from here
print(series.dtype)
print(series.count())
