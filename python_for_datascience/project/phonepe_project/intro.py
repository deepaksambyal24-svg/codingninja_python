import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


excel=pd.ExcelFile('phonepe.xlsx')
print(excel.sheet_names)
state_txn_users=pd.read_excel('phonepe.xlsx', sheet_name='State_Txn and Users')
state_txn_split=pd.read_excel('phonepe.xlsx', sheet_name='State_TxnSplit')
state_device_date=pd.read_excel('phonepe.xlsx', sheet_name='State_DeviceData')
district_txn_and_users=pd.read_excel('phonepe.xlsx', sheet_name='District_Txn and Users')
district