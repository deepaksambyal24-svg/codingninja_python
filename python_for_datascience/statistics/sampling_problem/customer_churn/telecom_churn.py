import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('telecom_churn.csv')
print(df.head().T)
print(df.shape)

mc_mean=df['monthly_charges'].mean()
print(mc_mean)
mc_std=df['monthly_charges'].std()
print(mc_std)

df['standard_value']=(df['monthly_charges']-mc_mean)/mc_std
print(df['standard_value'].head())

sns.histplot(data=df, x='standard_value', bins=10, kde=True)
plt.xlabel('Standardized Monthly Charges')
plt.ylabel('Frequency')
plt.title('Distribution of Standardized Monthly Charges')
plt.show()


#select random sample of
survey_sample=df['monthly_charges'].sample(n=100, random_state=42)
obs_sample=df['total_charges'].sample(n=100, random_state=42)
print(survey_sample.head())

print(obs_sample.head())

sns.histplot(survey_sample, bins=10, kde=True)
plt.xlabel('Monthly Charges')
plt.ylabel('Frequency')
plt.title('Distribution of Monthly Charges in Survey Sample')
plt.show()
sns.histplot(obs_sample, bins=10, kde=True)
plt.xlabel('Total Charges')
plt.ylabel('Frequency')
plt.title('Distribution of Total Charges in Observation Sample')
plt.show()


# stratified sampling based on churn status
reg=df['region'].value_counts()
print(reg)
stratified_sample=df.groupby('region',observed=True).sample(n=100, random_state=42)
print(stratified_sample)

print(f'Mean total charges by region: {stratified_sample.groupby("region")["total_charges"].mean()}')
print(f'Overall mean total charges of the stratified sample: {stratified_sample["total_charges"].mean()}')

#  bar chart

int_ser=df['internet_service'].value_counts()
print(int_ser)
plt.figure(figsize=(10,5))
sns.barplot(x=int_ser.index, y=int_ser.values,color='blue')
plt.xlabel('Internet Service ')
plt.ylabel('Count')
plt.title('Distribution of Internet Service')
plt.show()



# kernal desity estimation plot
sns.histplot(data=df, x='monthly_charges', color='blue',bins=10, kde=True)
plt.xlabel('Monthly Charges')
plt.ylabel('Density')
plt.title('Kernel Density Estimation of Monthly Charges')
plt.show()