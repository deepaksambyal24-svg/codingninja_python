import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('student_data.csv')
print(df.T)

# averagestudytime for each famsize catetory
avg_stuty=df.groupby('famsize')['studytime'].mean().reset_index()
print(avg_stuty)
sns.barplot(x='famsize', y='studytime', data=avg_stuty)
plt.title('Average Studies')
plt.xlabel('Family Size')
plt.ylabel('Average Study Time')
plt.show()

# distribution of students ages
age_dist=df['age'].value_counts().sort_index()
plt.figure(figsize=(10,6))
sns.barplot(x=age_dist.index, y=age_dist.values)
plt.title('Distribution of Students Ages')
plt.xlabel('Age')
plt.ylabel('Number of Students')
plt.show()


 
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('student_data.csv')

# Plot the histogram for 'age'
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Distribution of Students by Age', fontsize=16)
plt.grid(axis='y', alpha=0.75)

# Display the histogram
plt.show()
