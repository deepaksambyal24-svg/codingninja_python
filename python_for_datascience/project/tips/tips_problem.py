import pandas as pd

import matplotlib.pyplot as plt
from fontTools.merge import cmap
from matplotlib.lines import Line2D



df=pd.read_csv("tips.csv")

print(df)
customer_count=df['day'].value_counts()
plt.figure(figsize=(10,5))
customer_count.plot(kind='bar',color='blue' )
plt.title('Customer Count')
plt.xlabel('day',fontsize=15)
plt.ylabel('Customer Count',fontsize=15)
plt.xticks(rotation=90)
plt.tight_layout()



plt.show()
avg_tips= df['tip'].groupby(df['day']).mean()
plt.figure(figsize=(10,5))
plt.bar(avg_tips.index, avg_tips.values, color='blue')
plt.title('Average Tips')
plt.xlabel('day',fontsize=15)
plt.ylabel('Average Tips')
plt.show()


# using seaborn and plot pi chart
import seaborn as sns
weekday_gender=df[df['day'].isin(['Thur','Fri'])]
gender_distribution= weekday_gender['sex'].value_counts()
plt.pie(gender_distribution.values,labels=gender_distribution.index,autopct='%1.1f%%',startangle=90)
plt.title('Gender Distribution')
plt.show()




# plotting the the scatter plot
plt.figure(figsize=(10,5))
female_lunch=df[(df['sex'] == 'Female') & (df['time'] == 'Lunch')]
female_dinner=df[(df['sex'] == 'Female') & (df['time'] == 'Dinner')]
male_lunch=df[(df['sex'] == 'Male') & (df['time'] == 'Lunch')]
male_dinner=df[(df['sex'] == 'Male') & (df['time'] == 'Dinner')]

plt.figure(figsize=(10,5))
plt.scatter(female_lunch['total_bill'],female_lunch['tip'],color='blue',marker='x')
plt.scatter(female_dinner['total_bill'],female_dinner['tip'],color='blue',marker='o')
plt.scatter(male_lunch['total_bill'],male_lunch['tip'],color='orange',marker='x')
plt.scatter(male_dinner['total_bill'],male_dinner['tip'],color='orange',marker='o')

plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.title('Scatter Plot of Total Bill vs Tip')
# Legend for SEX
sex_legend = [
    Line2D([], [], marker='o', color='blue',
           linestyle='None', label='Female'),

    Line2D([], [], marker='o', color='orange',
           linestyle='None', label='Male')
]

legend1 = plt.legend(
    handles=sex_legend,
    title='sex',
    loc='upper left'
)

# Legend for TIME
time_legend = [
    Line2D([], [], marker='o', color='black',
           linestyle='None', label='Dinner'),

    Line2D([], [], marker='x', color='black',
           linestyle='None', label='Lunch')
]

legend2 = plt.legend(
    handles=time_legend,
    title='time',
    loc='upper left',
    bbox_to_anchor=(0, 0.82)
)

# Keep both legends
plt.gca().add_artist(legend1)


# Keep both legends
plt.gca().add_artist(legend1)

plt.show()


# same plot using seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = pd.read_csv("tips.csv")

# Create a scatter plot for total bill vs tip
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', style='time')

# Set the title and labels
plt.title('Scatter Plot of Total Bill vs Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')

# Display the plot
plt.show()

# creating a bar chart
plt.figure(figsize=(8,6))
sns.barplot(data=df,x='day',y='total_bill',estimator='mean',hue='sex')
plt.xlabel('Day of the Week',fontsize=15)
plt.ylabel('Average Total Bill ($)',fontsize=15)
plt.title('Average Total Bill by Day of the Week.',fontsize=15)
plt.xticks(rotation=45)
plt.show()



#display the scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x='total_bill',y='tip',hue='time',style='sex',)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill ($)',fontsize=15)
plt.ylabel('Tip ($)',fontsize=15)
plt.show()




# creating a heatmap using seaborn








# plt.xticks(rotation=90)}+?"
df=sns.load_dataset('tips')

corr=df.corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(data=corr,annot=True,cmap='coolwarm',cbar=True,fmt='.1f')
plt.title('Correlation Matrix of Tips Dataset',fontsize=14)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()

# distribution of gender
gend_count=df['sex'].value_counts()
fig,axes=plt.subplots(2,2,figsize=(12,12))
days=df['day'].unique().tolist()
print(days)
colors = {
    'Thur': ['#66b3ff', '#99ff99'],
    'Fri': ['#ffcc99', '#c2c2f0'],
    'Sat': ['#ff6666', '#99ccff'],
    'Sun': ['#ffb3e6', '#c2f0c2']
}
for index,day in enumerate(days):
     subset=df[df['day']==day]
     sex_count=subset['sex'].value_counts()
     ax=axes[index//2,index%2]    # ax=axes=[row,column]
     ax.pie(x=sex_count.values,labels=sex_count.index,autopct='%1.1f%%',startangle=90,colors=colors[day])
     ax.set_title(f'Gender Distribution on {day}')
     ax.legend()
plt.tight_layout()
plt.show()




