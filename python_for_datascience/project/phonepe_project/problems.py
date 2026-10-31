import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats
from scipy.constants import alpha

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

    print(numeric_data.describe().to_string(float_format=lambda x: f'{x:,.2f}'))
    print('\n' * 3)
    print('=' * 80)
# # 1.3) ----> check for missing values
# # identify the missing vlaues
for name, df in dfs.items():
    print(f'\nDataFrame: {name}')
    print(f'Has null values:\n{df.isnull().sum()}')
    print('\n' * 3)
    print('=' * 80)
# # calculate the percentage of missing values
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
        print('\n' * 3)
        print('=' * 80)
# # 1.4 ----> create a summary
# # A) calculate the total number of states and total number of districts
state_count=district_txn['State'].nunique()
print(f' The Total numbers of states in our Dataframes are : {state_count}')
district_count=district_txn['District'].nunique()
print('\n' * 3)
print(f' The Total numbers of districts in our Dataframes are : {district_count}')
print('\n' * 3)
print('=' * 80)

# # B) -----> identify the state with highest number of districts
highest_district_state=demography.drop_duplicates(['State','District'])['State'].value_counts()
print(f'State with highest number of districts is : {highest_district_state.idxmax()}')
print('\n' * 3)
print('=' * 80)
#
# ###########################################################################################################################
# # TASK 2 ----->
#
# # 2.1) EDA
#
# # calculate the total number of transactions and total transaction amount for each state over the years
transactions_trends=txn.groupby(['State','Year']).agg(Total_transactions=('Transactions','sum'),
                        Total_amount=('Amount (INR)','sum')).sort_values(by='Total_transactions',ascending=False).reset_index()
transactions_trends['Total_Amt_crore']=(transactions_trends['Total_amount']/1e7).round(2)  # 1e7 mean 1 raise to power 7 ie 1 cr
transactions_trends.drop(columns=['Total_amount'], inplace=True)
transactions_trends.index=range(1,len(transactions_trends)+1)
print(transactions_trends)

print('\n' * 3)
print('=' * 80)
#
# # top 5 state with highest transaction volume
top5_volume=transactions_trends.groupby('State')['Total_transactions'].sum().nlargest(5) .reset_index()
top5_volume.index=range(1,len(top5_volume)+1)
print('\n The top 5 states with highest volume are:')
print(top5_volume)

print('\n' * 3)
print('=' * 80)
# # top 5 states with lowest transaction volumes
bottom_5_volume=transactions_trends.groupby('State')['Total_transactions'].sum().nsmallest(5).reset_index()
bottom_5_volume.index=range(1,len(bottom_5_volume)+1)
print('\n The bottom 5 states with lowest volume are:')
print(bottom_5_volume)
#
#
# # 2.2) ----> Identify the most common transaction types in each state and quarter
#
txn_counts=txn_type.groupby(['State','Quarter','Transaction Type']).size()
most_freq_txn_type = ( txn_counts.reset_index(name='Count').sort_values('Count', ascending=False)
    .drop_duplicates(['State', 'Quarter']).sort_values(['State', 'Quarter']).reset_index(drop=True))
most_freq_txn_type.index=range(1,len(most_freq_txn_type)+1)
print(f'\n The most frequent transaction type for each state and quarter  are:')
most_common = txn_type['Transaction Type'].value_counts()
print(f'The most frequent transaction type for each state and quarter  is :{most_common.index[0]}')
print('\n' * 3)
print('=' * 80)
#
# # 2.3) ----> Determine the device brand with the highest number of registered users in each state
ttl_users=device_data.groupby(['State','Brand'])['Registered Users'].sum().reset_index(name='Count')

res=ttl_users.groupby('State')['Count'].idxmax()
highest_user_device=ttl_users.loc[res].sort_values(by='Count', ascending=False)
highest_user_device.index=range(1,len(highest_user_device)+1)
print(f'\n The Device Brand with highest number of users is :')
print(highest_user_device)
print('\n' * 3)
print('=' * 80)
#
#
# # 2.4) -----> create a list of top district per state based on population
dist_pop=demography.groupby(['State','District'])['Population'].sum().reset_index()
high_dist_idx=dist_pop.groupby('State')['Population'].idxmax()
highes_pop_dist=dist_pop.loc[high_dist_idx].reset_index(drop=True)

print(f'\n The State with the highest population  is :')


# 2) CREATE A COLUMN CHART FOR THIS
highes_pop_dist=highes_pop_dist.sort_values(by='Population', ascending=False)
highes_pop_dist.index=range(1,len(highes_pop_dist)+1)
print(highes_pop_dist)
plt.figure(figsize=(10,5))
sns.barplot(data=highes_pop_dist,x='District',y='Population')
plt.title('Most Populous District in Each State', fontsize=16)
plt.xlabel('State')
plt.ylabel('Population')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print('\n' * 3)
print('=' * 80)
#
#
# # # 2.5 ) -----> calculate the average transaction value ( atv for each state
average_txn_value= txn.groupby('State').agg(Total_transactions=('Transactions','sum'),Total_amount=('Amount (INR)','sum')).reset_index()
average_txn_value['AVT PER STATE']=average_txn_value['Total_amount']/average_txn_value['Total_transactions']
average_txn_value=average_txn_value.sort_values(by='AVT PER STATE',ascending=False).reset_index(drop=True)
#
print(f'\n The  top 5 average transaction value per states are :')
top_5 = average_txn_value[['State', 'AVT PER STATE']].nlargest(5, 'AVT PER STATE').reset_index(drop=True).round(2)
top_5.index = range(1, len(top_5) + 1)
print(top_5)
print(f'\n The bottom 5 average transaction value per states are :')
bottom_5 = average_txn_value[['State', 'AVT PER STATE']].nsmallest(5, 'AVT PER STATE').reset_index(drop=True).round(2)
bottom_5.index = range(1, len(bottom_5) + 1)
print(bottom_5)
print('\n' * 3)
print('=' * 80)
# #
# # # 2.6) ---> analyze app usage trends
ttl_app_open=txn.groupby(['State','Year','Quarter'])['App Opens'].sum( ).reset_index(name='total_opens')
ttl_app_open.sort_values(['State','Year','Quarter'],ascending=[1,1,0],inplace=True)
print(ttl_app_open)
print('\n' * 3)
print('=' * 80)
# ploting the line plot showing the number of app opnes over time for a selected state
import seaborn as sns
import matplotlib.pyplot as plt
states=ttl_app_open['State'].unique()
# i am looping over each state inplace of choosing only one state
#
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
# print('\n' * 3)
# print('=' * 80)
# # 2.7) -------. distribution of transaction types
#
recent_year=txn_type['Year'].max()
recent_qtr=txn_type.loc[txn_type['Year']==recent_year,'Quarter'].max()
filter_d=txn_type[(txn_type['Year']==recent_year) & (txn_type['Quarter']==recent_qtr)]

txn_distribution = filter_d.groupby(['State', 'Transaction Type']).size().reset_index(name='Count')

plt.figure(figsize=(10, 5))
sns.barplot(data=txn_distribution, x='State', y='Count', hue='Transaction Type')
plt.title('Distribution of Transaction Types by State')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print('\n' * 3)
print('=' * 80)

# # 2.8) ------> Find unique Mapping between district name and district code
#
# # a) --> identify the uniqye mapping between district names and district code
code_dist=demography.drop_duplicates(subset=demography[['District','Code']],keep='first')[['State','District','Code']]
code_dist.index=range(1,len(code_dist)+1)
import os
file_name='district_code_mapping.csv'

if os.path.exists(file_name):
    print('File exists')
else:
    code_dist.to_csv('district_code_mapping.csv',index=False)
print('\n' * 3)
print('=' * 80)

# ########################################################################################################################
# # TASK 3 --------->
#
# # 3.1 ) ---> ENSURE DATA CONSISTENCY ACROSS STATE AND DISTRICT LEVELS
summary_user=pd.pivot_table(data=district_txn,index='State',values=
['Transactions','Amount (INR)','Registered Users'],
               aggfunc={'Transactions':'sum','Amount (INR)':'sum','Registered Users':'sum'})

summary_user = summary_user.rename(columns={'Transactions': 'Total_txns','Amount (INR)': 'Total_amt_(CR)','Registered Users': 'Total_reg_user'})

summary_user['Total_amt_(CR)']=(summary_user['Total_amt_(CR)']/10000000).round(2)
summary_user = summary_user.reset_index()
summary_user.index = range(1, len(summary_user) + 1)

print(summary_user)
# Top 5 states by total transactions
top_txns = summary_user.nlargest(5, 'Total_txns')
# Top 5 states by total transaction amount
top_amount = summary_user.nlargest(5, 'Total_amt_(CR)')
# Top 5 states by registered users
top_users = summary_user.nlargest(5, 'Total_reg_user')
print("Top 5 States by Transactions")
top_txns.index = range(1, len(top_txns) + 1)
print(top_txns.to_string())
print("\nTop 5 States by Transaction Amount")

top_amount.index = range(1, len(top_amount) + 1)
print(top_amount.to_string())
print("\nTop 5 States by Registered Users")

top_users.index = range(1, len(top_users) + 1)
print(top_users.to_string())
# Bottom 5 states by total transactions
bottom_txns = summary_user.nsmallest(5, 'Total_txns')
# Bottom 5 states by total transaction amount
bottom_amount = summary_user.nsmallest(5, 'Total_amt_(CR)')
# Bottom 5 states by registered users
bottom_users = summary_user.nsmallest(5, 'Total_reg_user')
print("\nBottom 5 States by Transactions")
bottom_txns.index = range(1, len(bottom_txns) + 1)
print(bottom_txns.to_string())
print("\nBottom 5 States by Transaction Amount")
bottom_amount.index = range(1, len(bottom_amount) + 1)
print(bottom_amount.to_string())
print("\nBottom 5 States by Registered Users")
bottom_users.index = range(1, len(bottom_users) + 1)
print(bottom_users.to_string())
print('\n' * 3)
print('=' * 80)
#
# # B) ----> STATE LEVEL
print(f'Summarizing the state-level data for comparison')
state_level=pd.pivot_table(data=txn,index='State',values=['Transactions','Amount (INR)'],aggfunc={'Transactions':'sum','Amount (INR)':'sum'},)

state_level=state_level.rename(columns={'Transactions':'Total_state_txns','Amount (INR)':'Total_state_amount_cr'})
state_level['Total_state_amount_cr'] = ( state_level['Total_state_amount_cr'] / 10000000).round(2)
state_level = state_level.reset_index()
state_level.index = range(1, len(state_level) + 1)
print(state_level)
print('\n' * 3)
print('=' * 80)

#
# # 3 ) --- find the discrepancies in both State and district data
compare_data = pd.merge(summary_user,state_level,on='State',how='outer',indicator=True)
compare_data['Txn_Difference'] = (compare_data['Total_txns'] - compare_data['Total_state_txns'])
compare_data['Amount_Difference_CR'] = (compare_data['Total_amt_(CR)'] - compare_data['Total_state_amount_cr']).round(2)
compare_data['Txn_Status'] = np.where(compare_data['Txn_Difference'] > 0,'District-level is greater',
    np.where( compare_data['Txn_Difference'] < 0,'State-level is greater', 'Both are equal' ))
compare_data.index = range(1, len(compare_data) + 1)
print(compare_data[['State', 'Txn_Difference', 'Txn_Status']])
print('\n' * 3)
print('=' * 80)

#
# ########################################################################################################################
# # TASK 4 ------- >Data merging and Advanced Analysis
#
# #1 --- merge the district_txn_uers and district demographics
#
# # summarize the total users for each state
# state_users = txn.groupby('State')['Registered Users'].sum()
# state_users = state_users.rename('Total_users').reset_index()
# state_users.index = range(1, len(state_users) + 1)
# print(state_users)
# print('\n' * 3)
# print('=' * 80)
# #
# # found users dataframe has  cumulative sum hence change the code
#
# # Sort the data by year and quarter
txn_sorted = txn.sort_values(['Year', 'Quarter'])
latest_users = txn_sorted.groupby('State').tail(1)
state_users = latest_users[['State', 'Registered Users']].copy()
state_users = state_users.rename(columns={'Registered Users': 'Total_users'})
print(state_users)
print('\n' * 3)
print('=' * 80)
#
# # summarize the total population form demo
state_pop=demography.groupby('State')['Population'].sum()
state_pop=state_pop.rename('Total_population').reset_index()
state_pop.index = range(1, len(state_pop) + 1)
print(state_pop)
print('\n' * 3)
print('=' * 80)
#
# # merge both for calculating the ration
users_pop_table=pd.merge(state_users,state_pop,on='State',how='inner')
users_pop_table.index = range(1, len(users_pop_table) + 1)
users_pop_table['Users_Pop_ratio']=round((users_pop_table['Total_users']/users_pop_table['Total_population'])*100,2)
print(users_pop_table)
print('\n' * 3)
print('=' * 80)
#
# # 2 ) -----> creating a column chart depicting the ratio of users to population by state
users_pop_table.sort_values( by='Users_Pop_ratio',ascending=False,inplace=True)
sns.barplot(data=users_pop_table,x='State',y='Users_Pop_ratio')
plt.xticks(rotation=90)
plt.title('Registered Users to Population Ratio by State')
plt.xlabel('State')
plt.ylabel('Users-to-Population Ratio (%)')
plt.tight_layout()
plt.show()
print('\n' * 3)
print('=' * 80)
#
#
# # 4.2 ) ----------> Correlated population density with transaction volume
#
# #   A ) merge the district_txn_users dataset with the District Demographics
#
#
dist_Corr=pd.merge(district_txn,demography[['Code','Density']],on='Code',how='left')[['State','Transactions','Density']]
print(district_txn.shape)
print(dist_Corr.shape)
corelation = dist_Corr['Density'].corr(dist_Corr['Transactions'])
print(f' The correlation between the population Density & Transaction voulume is : { corelation.round(2)}')
print('\n' * 3)
print('=' * 80)
#
#
# # 3) ---- creating a scatter plot to visualize the correlation
#
sns.scatterplot(data=dist_Corr,x='Density',y='Transactions',color='teal',alpha=0.7,edgecolor='black')
plt.title('Population Density vs Transaction Volume', fontsize=16)
plt.xlabel('Population Density (people per sq. km)', fontsize=12)
plt.ylabel('Transaction Volume', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
#
# #######################################################################################################################
# # TASK 4.3) ------> Average transactions amount per user
# # BECAUSE IN STATE TXN TABLE AMOUNT IS CUMULATIVE FOR EACH QUARTER I USER THE DISTRICT WISE TXN TABLE FOR
# # TRANSACTION AMOUNT AND DEVICE DATA TABLE FOR USER DATA
#
# '''i found that in state transaction tables amount is cumulative so each quarter add the previous amount to next quarter
# if i take that amount fron the table it would be incorrect insight so i choose the district table for this and group by the
# state to summarize the total amount and also found other data has no mismatching users data is same on all the table users are total
#    of 2,40,78,60,447 on all tables '''
amount_state=district_txn.groupby('State')['Amount (INR)'].sum().reset_index()
ttl_u=device_data.groupby('State')['Registered Users'].sum().reset_index()
amount_state = amount_state.rename(columns={'Amount (INR)': 'Total_Amount'})
ttl_u = ttl_u.rename(columns={'Registered Users': 'Total_Users'})
avg_trans = pd.merge(amount_state, ttl_u, on='State', how='inner')
avg_trans['avg_txn_per_user'] = (avg_trans['Total_Amount'] / avg_trans['Total_Users']).round(2)

top_5=avg_trans.nlargest(5,'avg_txn_per_user').reset_index(drop=True)
top_5.index = range(1, len(top_5) + 1)
print("Top 5 States by Average Transaction Amount per User:")
print(top_5)
print('\n' * 3)
print('=' * 80)
#

lowest_5=avg_trans.nsmallest(5,'avg_txn_per_user').reset_index(drop=True)
lowest_5.index = range(1, len(lowest_5) + 1)
print("Top 5 States having lowest Average Transaction Amount per User:")
print(lowest_5)
print('\n' * 3)
print('=' * 80)

#
# # ###################################################################################################################
# # 4.4 ) -----> Device brand usage ratio
#
total_user_in_state=txn.groupby('State')['Registered Users'].sum().reset_index()
user_using_devices=device_data.groupby(['State','Brand'])['Registered Users'].sum().reset_index()
df=pd.merge(total_user_in_state,user_using_devices,on='State',how='left',suffixes=('_state','_device'))
df = df.rename(columns={'Registered Users_device': 'Total_Devices','Registered Users_state': 'Total_Users'})
df = df[['State', 'Brand', 'Total_Devices', 'Total_Users']]
df['Device_brand_ratio'] = (df['Total_Devices'] / df['Total_Users'] * 100).round(2)
df.index = range(1, len(df.index) + 1)
print(df.T)
print('\n' * 3)
print('=' * 80)

#
# # 3 ) -----> ploting the bar chart
df_sorted = df.sort_values(by=['State', 'Device_brand_ratio'],ascending=[True, True])
plt.figure(figsize=(20, 8))
sns.barplot( data=df, x='State',y='Device_brand_ratio',hue='Brand')
plt.title('Device Brand Usage Ratio by State', fontsize=16)
plt.xlabel('State', fontsize=12)
plt.ylabel('Device Usage Ratio (%)', fontsize=12)
plt.xticks(rotation=90, fontsize=9)
plt.yticks(fontsize=10)
plt.legend(title='Device Brand', bbox_to_anchor=(1.02, 1), loc='upper left',fontsize=9)
plt.tight_layout()
plt.show()
print('\n' * 3)
print('=' * 80)


# ########################################################################################################################
# # TASK 5 ------> DATA VISUALIZATION
#
# # 5.1 )  plot the transaction and amount over time for a selected state
#
state='Himachal Pradesh'
my_df=txn[(txn['State']==state) ].copy().reset_index()
my_df=my_df.sort_values(['Year','Quarter'])
my_df['Amount (Cr)'] = my_df['Amount (INR)'] / 10000000
my_df['year_Q']=(my_df['Year'].astype(str) + "-Q" + my_df['Quarter'].astype(str))
print(my_df.T)
print('\n' * 3)
print('=' * 80)

#
# # ploting a line chart over time
#
# plt.figure(figsize=(16, 8))
# plt.plot(my_df['year_Q'], my_df['Transactions'], color='blue', marker='o', label='Total Transactions')
# plt.plot(my_df['year_Q'], my_df['Amount (INR)'], color='red', marker='o', label='Transaction Amount')
# plt.title(f'Transaction Count and Amount Over Time - {state}')
# plt.xlabel('Year and Quarter')
# plt.ylabel('Values')
# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
#
# '''because i have two variables for ploting line chart and both are on different scale for income got a straight line
# becasue it is dominating hence i plot line chart on dual y axis '''
fig, ax1 = plt.subplots(figsize=(16, 8))
sns.lineplot(  data=my_df, x='year_Q', y='Transactions', ax=ax1,color='blue', marker='o',legend=False)
ax1.set_ylabel('Total Transactions', color='blue')
ax2 = ax1.twinx()
sns.lineplot( data=my_df, x='year_Q', y='Amount (INR)',ax=ax2,color='red', marker='o', legend=False)
ax2.set_ylabel('Transaction Amount (INR)', color='red')
ax1.legend(  [ax1.lines[0], ax2.lines[0]],['Total Transactions', 'Transaction Amount (INR)'], loc='upper left')
plt.title(f'Transaction Count and Amount Over Time - {state}')
ax1.set_xlabel('Year and Quarter')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print('\n' * 3)
print('=' * 80)
#
#
# # 5.2 ) ----> create a pie chart showing the distribution of transaction types for a specific quarter
#
my_df2=txn_type[txn_type['State']==state].copy().reset_index()
type_dis=my_df2['Transaction Type'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(  type_dis.values, labels=type_dis.index, autopct='%1.1f%%',startangle=90)
plt.title(f'Transaction Type Distribution by State', fontsize=16)
plt.show()
print('\n' * 3)
print('=' * 80)
#
#
# # 5.3 ----> visualize the population density of districts in a selected state
my_state_districts = demography[demography['State'] == state][['District', 'Density']].copy()
my_state_districts = my_state_districts.sort_values( by='Density', ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot( data=my_state_districts,x='District', y='Density')
plt.title(f'Population Density of Districts in {state}', fontsize=16)
plt.xlabel('District')
plt.ylabel('Population Density (people per sq km)')
plt.xticks(rotation=90, fontsize=10)
plt.tight_layout()
plt.show()
print('\n' * 3)
print('=' * 80)
#
# ########################################################################################################################
# # 1 ) identify any treands or patterns in the transaction data
# ''' i observed that there is consistent growth in digital payments , appox .5 million in Q1 2018 to 9.4 million
# in Q2 2021 and Transaction amount also increased
# B) there is strong growth in 2020
# c) transaction also relatively slow in q4 2020 and q1 2021
# d) transaction amount follows the transaction volume
# e) the strongest performane is in q2 2021
# CONCLUSION : ---> more transaction may indicates increasing acceptance of phone pe amount cunsumers and merchant . the
# business could investigate that after every 5 quarter there is a cross over between these lines means there is seasonal
# slow down . what are the factor beside it. '''
#
#
# # 2 ) correlate demographic data with transaction data
pop_den = demography.groupby('State')['Density'].mean().reset_index()
pop_den = pop_den.rename(columns={'Density': 'Density'})
txn_volume = txn.groupby('State')['Transactions'].sum().reset_index()
corr_df = pd.merge(pop_den, txn_volume,on='State',how='inner')
correlation = corr_df['Density'].corr(corr_df['Transactions'])
print(f'Correlation between population density and transaction volume: {correlation:.2f}')
# # which is close to zero hence state with higher average pop density dont necesarilu have highter total transaction
