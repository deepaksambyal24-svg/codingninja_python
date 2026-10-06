import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('Customer_Churn.csv')
print(df.T)
avg_bal=pd.pivot_table(df,index='Exited',values='Balance',aggfunc=np.mean)
print(avg_bal)
# plot the chart for this
sns.barplot(x=avg_bal.index,y=avg_bal['Balance'])
plt.xticks(rotation=90)
plt.ylabel('Balance')
plt.xlabel('Exited')
plt.tight_layout()
plt.title('Balance vs Exited')
plt.show()


#
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



sns.violinplot(
    data=df,
    x='NumOfProducts',
    y='CreditScore',
    hue='Exited',
    split=True
)

plt.title('Credit Score Distribution by Number of Products and Churn Status')
plt.xlabel('Number of Products')
plt.ylabel('Credit Score')
plt.show()

# CALCULATE THE CORRELATION BETWEEN NUMOFPRODUCTS AND CREDITSCORE
corr=df.corr(numeric_only=True)['Complain'].sort_values(ascending=False)
print(corr)
import matplotlib.pyplot as plt

corr = (
    df.corr(numeric_only=True)['Complain']
    .drop('Complain')
    .abs()
    .sort_values(ascending=True)
)

corr.plot(kind='barh')

plt.xlabel('Absolute Correlation with Complaint')
plt.ylabel('Feature')
plt.title('Features Most Correlated with Customer Complaints')
plt.show()


# creating the heat map for the same
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Select numerical columns and calculate correlation
corr_matrix = df.select_dtypes(include='number').corr()

# Create correlation heatmap
plt.figure(figsize=(10, 6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlation Heatmap')
plt.show()

# highest proportion of churned customers
churn_rate = df.groupby('Geography')['Exited'].mean()

second_highest = churn_rate.sort_values(ascending=False).iloc[1]

print(second_highest)
import matplotlib.pyplot as plt

churn_rate = df.groupby('Geography')['Exited'].mean()

churn_rate = churn_rate.sort_values(ascending=False)
print(churn_rate)

churn_rate.plot(kind='bar')

plt.xlabel('Geography')
plt.ylabel('Churn Proportion')
plt.title('Churn Proportion by Geography')
plt.show()


churned_df = df[df['Exited'] == 1]

# Count plot of churned customers by Geography
sns.countplot(
    data=churned_df,
    x='Geography',
    order=df['Geography'].value_counts().index
)

plt.title('Churned Customers by Geography')
plt.xlabel('Geography')
plt.ylabel('Count')

plt.show()

#