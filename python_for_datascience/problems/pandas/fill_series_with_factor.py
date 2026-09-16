# Write your code from here
import pandas as pd
i = 1
fac = []
while i <= 365:
    if 365 % i == 0:

        fac.append(i)
        i += 1
    else:

        i += 1
series =pd.Series(fac)
print(series)
