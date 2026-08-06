#   iterates fuction are ---> .keys ()      .values()        . items ()
from DIctionary.iteration_ofdictionary import new_cart

car={1:'Apple',2:'Banana',3:'Mango'}
for key in car:
    print(key,end='\t')
    print()

for value in car.values():
    print(value,end='\t')
    print()

for key,value in car.items():
    print(key,value,sep=':')
    print()


new_cart=car.copy()
print(new_cart)
print(id(new_cart))
print(id(car))