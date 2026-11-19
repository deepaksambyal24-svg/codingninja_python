product_name = "samsung phone"
price = 10000
def pay_for_product():
    global price
    product_name = "nokia"
    price = 5000
    print("paying for product", product_name,price)
pay_for_product()
print (product_name,price)