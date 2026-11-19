try:
    f=oper("temp.txt")
except(FileNotFoundError,PermissionError) as e:
    print("error occurred")
    print(e)

# Exception is base class for every exception
    # FilenotFound and PermisionError errors are the error of OS base class errors

try:
    f=open("temp.txt")
except OSError as e:
    print("error occurred")
    print(e) ## oserror  can handle both of them