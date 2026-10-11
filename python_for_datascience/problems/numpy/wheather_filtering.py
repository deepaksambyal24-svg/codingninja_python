import numpy as np

# Weekly temperature data (C)
temperatures = np.array([
    25, 32, 29, 35, 28, 31, 30, 27, 33, 34, 26, 29, 30, 32, 33,
    36, 28, 31, 30, 29, 35, 27, 28, 31, 34, 30, 29, 32, 35, 28,
    33, 26, 29, 30, 34, 32, 36, 28, 31, 30, 29, 33, 28, 30, 31,
    32, 34, 29, 27, 35, 31, 30, 28, 33, 34, 36, 29, 31, 30, 29,
    35, 28, 32, 30, 27, 33, 34, 28, 29, 32, 31, 30, 27, 35, 29,
    30, 32, 34, 31, 28, 33, 30, 29, 32, 36, 28, 35, 30, 29, 31,
    34, 32, 33, 28, 30, 29
])

# Define the threshold
threshold = 30

# Mask indexing to filter temperatures
mask=temperatures>threshold
filtered_temperatures = temperatures[mask]
print(f"Filtered temperatures greater than {threshold}C:", filtered_temperatures)