# Don't change the given lines of code
import numpy as np

# Given 2D NumPy array
data = np.array([[25, 180, 75],
                 [30, 175, 68],
                 [35, 170, 70],
                 [40, 165, 80]])

# 1. Extract the first two rows and the first two columns
subarray = data[:2,:2]
print("Extracted 2x2 Subarray:")
print(subarray)

# 2. Extract the last row of the array
last_row =  data[-1,::]
print(f"Last Row: {last_row}")

# 3. Extract all rows but only the second column
second_column = data[::,-2]
print(f"Second Column: {second_column}")