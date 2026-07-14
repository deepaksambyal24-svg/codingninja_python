# it has three keywords for iteration
# .keys () iteration on all keys
# .values () iteration on all values
# . items() iteration on all pairs

cart ={"101":3,"105":9,"112":2}
print(cart)
print(cart.keys())
print(cart.values())
print(cart.items())



# for iteration

for key in cart.keys():
    print(key)

#another method
for k in cart:
    print(k,cart[k])

#iteration on pairs
for pair in cart.items():
    print(pair)


# copy cart
new_cart=cart.copy()
print(id(cart),id(new_cart))