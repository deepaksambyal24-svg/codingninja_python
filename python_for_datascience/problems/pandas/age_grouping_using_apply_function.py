import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "age": [18, 25, 35, 42, 58, 60, 65, 29, 22, 50]
}
df = pd.DataFrame(data)


# Write your code here!
def grouping(x):
    if 18 <= x <= 21:
        return 'Group 1'
    elif 22 <= x <= 30:
        return 'Group 2'
    elif 31 <= x <= 45:
        return 'Group 3'
    elif 46 <= x <= 60:
        return 'Group 4'
    else:
        return 'Group 5'


df['age_group'] = df['age'].apply(grouping)
print(df)

