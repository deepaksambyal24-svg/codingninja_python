import numpy as np

# Write your code here
m=np.eye(7,dtype=int)
n=np.fliplr(m)
res=m+n
res[3,3]=1
print(res)