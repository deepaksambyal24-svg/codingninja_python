import pandas as pd

data = {
    "teacher_id": [1, 1, 2, 2, 1, 3],
    "teacher_name": ["Amit", "Amit", "Priya", "Priya", "Amit", "Kiran"],
    "subject": ["Mathematics", "Physics", "Chemistry", "Mathematics", "Mathematics", "Biology"]
}

TeachingRecords = pd.DataFrame(data)

# Write your code here
res = TeachingRecords.groupby(['teacher_id', 'teacher_name'])['subject'].nunique().reset_index(
    name='unique_subject_count')

print(res)