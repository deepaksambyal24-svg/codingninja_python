def square(x):
    return x*x
def add(x,y):
    return x+y
def cube(x):
    return x*x*x
def stock_status(qty,reorder_level=10):
    if qty ==0:
        return "out of stock"
    elif qty<reorder_level:
        return "low stock"
    else:
        return "in stock"
