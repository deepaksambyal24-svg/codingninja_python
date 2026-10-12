import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
df=pd.read_excel('phonepe.xlsx')

excel_file = pd.ExcelFile('phonepe.xlsx')

print(excel_file.sheet_names)
print("Total sheets:", len(excel_file.sheet_names))
txn_users=pd.read_excel('phonepe.xlsx',sheet_name='State_Txn and Users')
state_txn=pd.read_excel('phonepe.xlsx',sheet_name='State_TxnSplit')
device_data=pd.read_excel('phonepe.xlsx',sheet_name='State_DeviceData')
district_txn=pd.read_excel('phonepe.xlsx',sheet_name='District_Txn and Users')
demography=pd.read_excel('phonepe.xlsx',sheet_name='District Demographics')
admin=pd.read_excel('phonepe.xlsx',sheet_name='Admin')
print(txn_users.T)
print(state_txn.T)
print(device_data.T)
print(district_txn.T)
print(demography.T)
print(admin.T)
