from click import clear

di={'101': 'Alice','102':'deepa','103':'deepa','104':'Alice'}
print(di)
di.pop('101')
print(di)

del di['102']
print(di)
di.clear()


# Updating values for a given key

cart={101:'Apple',102:'Banana',103:'Mango'}
cart['103']=44
print(cart)
