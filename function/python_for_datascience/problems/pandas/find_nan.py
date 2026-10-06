import pandas as pd
import numpy as np

series1 = pd.Series([10, np.nan, 30, 40, 50, np.nan, 70])
series2 = pd.Series([2, 3, np.nan, 5, 6, 7, np.nan])

# Write your code from here
series1.hasnans
series2.hasnans
remove1=series1.dropna()
remove2=series2.dropna()
mul=remove1 * remove2
print(mul.fillna(-1))
