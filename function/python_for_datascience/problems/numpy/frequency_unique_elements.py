import numpy as np

# Array representing the scores of students
scores = np.array([85, 90, 85, 70, 95, 90, 85, 70, 80, 95])


# Calculate the frequency of each unique score
unique,arr=np.unique(scores, return_counts=True)
print(unique)
print(arr)