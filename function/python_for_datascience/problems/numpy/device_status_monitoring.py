import numpy as np

# Write your code here
active_dev = np.ones(15, dtype=int)

non_active_dev = np.zeros(5, dtype=int)

matrix = np.concatenate((active_dev, non_active_dev), axis=0)

matrix[12:15] = np.where(matrix[12:15] == 1, 0, 0)
active = np.sum(matrix == 1)
non_active = np.sum(matrix == 0)
print(f'Total Active Devices: {active}')
print(f'Total Inactive Devices: {non_active}')