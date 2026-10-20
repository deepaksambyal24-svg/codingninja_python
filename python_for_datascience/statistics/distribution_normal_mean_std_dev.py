import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.random.normal(loc=0,scale=1,size=10000)
plt.hist(data,bins=20,edgecolor='black')
plt.title('Histogram of normal distribution')
plt.xlabel('normal distribution')
plt.ylabel('Frequency')
plt.show()
