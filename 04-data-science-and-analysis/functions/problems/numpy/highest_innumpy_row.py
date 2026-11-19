import numpy as np

marks_data = np.array([[85, 90, 88],
                       [75, 80, 78],
                       [92, 95, 91],
                       [60, 65, 70]])

# Find the highest marks for each student (each row)
print(np.max(marks_data,axis=1))