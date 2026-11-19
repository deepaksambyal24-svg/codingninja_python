import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_excel('car_price_dataset.xlsx')
print(df.T)
data=df[['stroke','horsepower','enginesize','fueltype']]
print(data.T)
plt.figure(figsize=(10,5))
pair_plot=sns.pairplot(data=data,hue='fueltype',palette='coolwarm',markers=['o','s'],kind='reg',height=2.5)
pair_plot.fig.suptitle("Pair Plot of Numerical Features In Car Price Dataset by Fuel Type",y=1.02)
plt.show()