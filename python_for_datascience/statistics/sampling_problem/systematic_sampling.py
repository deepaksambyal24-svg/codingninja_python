import pandas as pd
df=pd.read_csv('systematic_data.csv')
systematic_sam=df.iloc[::5, :]
print(systematic_sam)