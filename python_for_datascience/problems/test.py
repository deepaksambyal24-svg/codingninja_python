cart_items = {"apple": (3, 5), "milk": (2, 2), "bread": (1.5, 3)}

discounts = {"apple": 10, "milk": 5}

delivery_charge = 3
for item in cart_items.items():
  if item[0] in discounts.keys():
    print(f'{item[0].capitalize()}- {item[1][1]} x ${item[1][0]} - {discounts[item[0]]}% discount = ${int(item[1][1] * item[1][0]) - (int(item[1][1] * item[1][0]) * discounts[item[0]] / 100)}')

  else:
    print(f'{item[0].capitalize()}- {item[1][1]} x ${item[1][0]} - 0% discount = ${item[1][1] * item[1][0]}')
print(f'Delivery Charge: ${delivery_charge}')
print(f'Total Bill: ${sum(float(item[1][1] * item[1][0]) - (float(item[1][1] * item[1][0]) * discounts.get(item[0], 0) / 100) for item in cart_items.items()) + delivery_charge}')



total = 0
for name, (price, qty) in cart_items.items():
    discount = discounts.get(name, 0)
    discounted_price = price * (1 - discount/100)
    item_total = discounted_price * qty
    print(f'{name.capitalize()} - {qty} x ${price} - {discount}% discount = ${item_total}')
    total += item_total
    print(f'Delivery Charge: ${delivery_charge}')
    total += delivery_charge
print(f'Total Bill: ${total}')