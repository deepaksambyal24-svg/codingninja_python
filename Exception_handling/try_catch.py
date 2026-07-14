try :
    a=2
    b=0
    res = a/b
    print("x") # if error occured this line never executed
except ZeroDivisionError as e :
    print( "this is a zero division error")
print("hello")

# an error stops the program execution
# but if i handle the error then program don't stop to excution


a = [1,2,3]
try :
    index =6
    res =a[index]
    print(f'element at index {index} is {res}')  # never executed

    print("hello")              # never executed
except IndexError:  # we gave the same exception other it stops the code execution

    print("index out of range")

a.append(10)
a.append(20)
print(a)
