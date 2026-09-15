import numpy as np

sales_data = np.array([[200, 400, 300],
                       [300, 500, 400],
                       [500, 600, 700],
                       [100, 200, 300]])

row_to_check = [300, 500, 400]

# Write your code here
for row in sales_data:
    if (row==row_to_check).all:
        print('Row is present.')
        break
    else:
        print('Row is not present.')
        continue