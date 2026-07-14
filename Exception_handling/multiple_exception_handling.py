try:
    a=[1,2,3,0]
    res=a[1]/a[3]
    except(IndexError,ZeroDivisionError):
    print("exception")
print("hello")


# or
# we can separtaly handle the exception
 try:
     a=[1,2,3,0]
     res=a[1]/a[3]
 except(IndexError):
     print("Index error exception")
 except ZeroDivisionError:
     print("ZeroDivisionError exception")
     # give different output
     
