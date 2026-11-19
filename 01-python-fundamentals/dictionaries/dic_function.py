cart={'101':10,"422":5,"17":3,"301":9}
print(cart)
cart.pop("101")             #remove 101
print(cart)
del cart ["17"]# does not return anything but remove key value pair
print(cart)

# for updating the value in key
cart["101"]=55
print(cart)