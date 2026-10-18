import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats
df=pd.read_excel('phonepe.xlsx')

excel_file = pd.ExcelFile('phonepe.xlsx')

print(excel_file.sheet_names)
print("Total sheets:", len(excel_file.sheet_names))
txn=pd.read_excel('phonepe.xlsx',sheet_name='State_Txn and Users')
txn_type=pd.read_excel('phonepe.xlsx',sheet_name='State_TxnSplit')
device_data=pd.read_excel('phonepe.xlsx',sheet_name='State_DeviceData')
district_txn=pd.read_excel('phonepe.xlsx',sheet_name='District_Txn and Users')
demography=pd.read_excel('phonepe.xlsx',sheet_name='District Demographics')
admin=pd.read_excel('phonepe.xlsx',sheet_name='Admin')
#######################################################################################################################
# TASK 1 : --------------------->
# 1.1) load each dataset and display its structure
print(txn.head(5))
print(txn_type.head(10))
# print the middle 5 rows  of the device data
mid=(device_data.shape[0])//2
print(device_data.iloc[mid-5:mid+5])

# display the first 10 rows and last 10 rows from district_txn_users DataFrame
res=pd.concat([district_txn.head(10),district_txn.tail(10)])
print(res)

# print every 10th row from district demographic dataFrame
res=demography[::10]
print(res)
#######################################################################################################################
# TASK 1-------------------------->


# 1.2)--->  print the summary statistics for numerical value and data types of each column in each DataFrame
dfs={'Transactions':txn,'Transactions_type':txn_type,'Device_data':device_data,'Districts_txns':district_txn,'Demography_Data':demography}
for name,df in dfs.items():
    print(df.dtypes)
    print(f'\n Summary for the DateFrame: {name}')
    numeric_data=df.select_dtypes(include='number')
    print(numeric_data.describe())


# 1.3) ----> check for missing values
# identify the missing vlaues
for name, df in dfs.items():
    print(f'\nDataFrame: {name}')
    print(f'Has null values:\n{df.isnull().sum()}')
# calculate the percentage of missing values
for name, df in dfs.items():
    print(f'\nPercentage of missing values in columns of DataFrame: {name}')
    missing_per = df.isnull().sum() / df.shape[0] * 100
    print(missing_per)
    if missing_per.max() == 0:
        print(f'The DataFrame: {name} has no missing values.')
    else:
        highest_column = missing_per.idxmax()
        highest_percentage = missing_per.max()
        print(f'The DataFrame: {name}, column: {highest_column} 'f'has the highest percentage of null values: {highest_percentage:.2f}%')

# 1.4 ----> create a summary
# A) calculate the total number of states and total number of districts
state_count=district_txn['State'].nunique()
print(f' The Total numbers of states in our Dataframes are : {state_count}')
district_count=district_txn['District'].nunique()
print(f' The Total numbers of districts in our Dataframes are : {district_count}')

# B) -----> identify the state with highest number of districts
highest_district_state=demography.drop_duplicates(['State','District'])['State'].value_counts()
print(f'State with highest number of districts is : {highest_district_state.idxmax()}')


###########################################################################################################################
# TASK 2 ----->

# 2.1) EDA

# calculate the total number of transactions and total transaction amount for each state over the years
transactions_trends=txn.groupby(['State','Year']).agg(Total_transactions=('Transactions','sum'),
                        Total_amount=('Amount (INR)','sum')).sort_values(by='Total_transactions',ascending=False).reset_index()
transactions_trends['Total_Amt_crore']=(transactions_trends['Total_amount']/1e7).round(2)  # 1e7 mean 1 raise to power 7 ie 1 cr
transactions_trends.drop(columns=['Total_amount'], inplace=True)

print(transactions_trends)

# top 5 state with highest transaction volume
top5_volume=transactions_trends.groupby('State')['Total_transactions'].sum().nlargest(5) .reset_index()
top5_volume.index=range(1,len(top5_volume)+1)
print('\n The top 5 states with highest volume are:')
print(top5_volume)

# top 5 states with lowest transaction volumes
bottom_5_volume=transactions_trends.groupby('State')['Total_transactions'].sum().nsmallest(5).reset_index()
bottom_5_volume.index=range(1,len(bottom_5_volume)+1)
print('\n The bottom 5 states with lowest volume are:')
print(bottom_5_volume)


# 2.2) ----> Identify the most common transaction types in each state and quarter

txn_counts=txn_type.groupby(['State','Quarter','Transaction Type']).size()
most_freq_txn_type = ( txn_counts.reset_index(name='Count').sort_values('Count', ascending=False)
    .drop_duplicates(['State', 'Quarter']).sort_values(['State', 'Quarter']).reset_index(drop=True))
print(f'\n The most frequent transaction type for each state and quarter  are:')
print(most_freq_txn_type)

# 2.3) ----> Determine the device brand with the highest number of registered users in each state
ttl_users=device_data.groupby(['State','Brand'])['Registered Users'].sum().reset_index(name='Count')

res=ttl_users.groupby('State')['Count'].idxmax()
highest_user_device=ttl_users.loc[res].sort_values(by='Count', ascending=False)
highest_user_device.index=range(1,len(highest_user_device)+1)
print(f'\n The Device Brand with highest number of users is :')
print(highest_user_device)


# 2.4) -----> create a list of top district per state based on population
dist_pop=demography.groupby(['State','District'])['Population'].sum().reset_index()
high_dist_idx=dist_pop.groupby('State')['Population'].idxmax()
highes_pop_dist=dist_pop.loc[high_dist_idx].reset_index(drop=True)
highes_pop_dist.index=range(1,len(highes_pop_dist)+1)
print(f'\n The State with the highest population  is :')
print(highes_pop_dist)



# 2.5 ) -----> calculate the average transaction value ( atv for each state
average_txn_value= txn.groupby('State').agg(Total_transactions=('Transactions','sum'),Total_amount=('Amount (INR)','sum')).reset_index()
average_txn_value['AVT PER STATE']=average_txn_value['Total_amount']/average_txn_value['Total_transactions']
average_txn_value=average_txn_value.sort_values(by='AVT PER STATE',ascending=False).reset_index(drop=True)

print(f'\n The  top 5 average transaction value per states are :')
top_5 = average_txn_value[['State', 'AVT PER STATE']].nlargest(5, 'AVT PER STATE').reset_index(drop=True).round(2)
top_5.index = range(1, len(top_5) + 1)
print(top_5)
print(f'\n The bottom 5 average transaction value per states are :')
bottom_5 = average_txn_value[['State', 'AVT PER STATE']].nsmallest(5, 'AVT PER STATE').reset_index(drop=True).round(2)
bottom_5.index = range(1, len(bottom_5) + 1)
print(bottom_5)

# 2.6) ---> analyze app usage trends
ttl_app_open=txn.groupby(['State','Year','Quarter'])['App Opens'].sum( ).reset_index(name='total_opens')
ttl_app_open.sort_values(['State','Year','Quarter'],ascending=[1,1,0],inplace=True)
print(ttl_app_open)

# ploting the line plot showing the number of app opnes over time for a slected state
import seaborn as sns
import matplotlib.pyplot as plt
states=ttl_app_open['State'].unique()
# i am looping over each state inplace of choosing only one state

# for state in states:
#     state_data=ttl_app_open[ttl_app_open['State']==state].copy()
#     state_data['total_open_lakh']=state_data['total_opens']/100000
#     state_data.sort_values(by=['Year','Quarter'],ascending=[1,1],inplace=True)
#     state_data['period']=(state_data['Year'] .astype(str) + 'Q'  + state_data['Quarter'] .astype(str))
#     print(state_data['period'])
#     plt.figure(figsize=(12, 6), dpi=100, facecolor='white')
#     sns.lineplot(data=state_data,x='period',y='total_open_lakh',marker='x',linewidth=2,color='blue' )
#     plt.xticks(rotation=90)
#     plt.title(f'App Opens Trend for the state - {state.upper()}',fontsize=20)
#     plt.xlabel('Year and Quarter')
#     plt.ylabel('Total App Opens in Lakh')
#     plt.xticks(rotation=90)
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()

# 2.7) -------. distribution of transaction types


