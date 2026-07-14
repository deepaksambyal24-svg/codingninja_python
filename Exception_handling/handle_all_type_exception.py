# we have common base class exception for handling all type of exceptions
try:
    a=[1,2,3,0]
    res=a[2]/a[6]
except Exception as e:
    print("exception occurred")
    print(e)  # print the exception typye for example index out of range
    
print("hello")
