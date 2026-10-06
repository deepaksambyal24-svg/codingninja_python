import numpy as np

data = {
    "Year": ["2015", "2016", "2017", "2018", "2019"],
    "Revenue": [1000, 1500, 2000, 2500, 3000],
    "Profit": [200, 250, 300, 350, 400],
    "Units_Sold": [100, 200, 300, 400, 500],
    "Employee_Name": ["Aliya", "Bablu", "Charlie", "Divendra", "Leena"]
}

# Write your code here
for key, values in data.items():
    if type(values[0]) == int:
        print(f'Numerical Column: {key}')
        print(f'Mean: {np.mean(values)}')
        print(f'Median: {np.median(values)}')
        print(f'Standard Deviation: {np.std(values)}')
        print(f'Minimum: {np.min(values)}')
        print(f'Maximum: {np.max(values)}')
        print(f'Sum: {np.sum(values)}\n')
