import pandas as pd
cars = pd.read_excel('car.xlsx')
print(cars.tail())
uni=cars.nunique()
print(uni)

res=cars[['street_num','city','state']]
print(res)
