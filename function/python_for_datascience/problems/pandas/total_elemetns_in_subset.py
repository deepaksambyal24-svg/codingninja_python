import pandas as pd
import numpy as np
df=pd.read_csv('train.csv')
ind=np.arange(2,10,2)
res=df.iloc[100,ind]
print(res.count().sum())