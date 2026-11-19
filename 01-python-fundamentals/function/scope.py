#scope is visibility of corresponding variable
product_name="samsung"          #global scope
price=19999
def pay_for_product():
    global price    # now can be updated
    product_name="lg"
    print("paying of product",product_name)
pay_for_product()           #local variable inside the funciton
print(product_name)  #global scope


# global keyword is used for access the variable
#global variable can be updated from inside function