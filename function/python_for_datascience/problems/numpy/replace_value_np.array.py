import numpy as np

# Write your code here

salary=np.full((5,10),50000,dtype=float)
salary[0]=salary[1]+.1*salary[0]
salary[2]=salary[2]-.05*salary[2]
print(np.array(salary).sum(axis=1))
print(np.array(salary).mean(axis=1))