#else block is executed if there is no excepton reached by try block
def f(a):
    try:
        a=2
        res = 10/a
    except ZeroDivisionError as e:
        print("division by zero")
    else:
        print("inside else")
        return res + 10

print(f(10))


# finally it will always execute the finally block not else block

try:
    a=0
    res = 10/a
    except ZeroDivisionError as e:
    print("division by zero")
    else:
        print("inside else")
    finally:
        print("inside finally")
 ## it will also goes to else block and also goes to finally block

 # finally always executed , use for closing of connections cleaning of resources etc
 
