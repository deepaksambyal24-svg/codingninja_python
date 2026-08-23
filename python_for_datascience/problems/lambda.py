def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

# The myfunc function takes an argument n and returns a lambda function that takes
# another argument a.
# 2. Inside the lambda function, a is multiplied by n.
# 3. When myfunc(3) is called, it returns a lambda function where n is 3. This lambda
# function effectively becomes lambda a: a * 3.
# 4. mytripler now refers to this lambda function.
# 5. When mytripler(11) is called, it's equivalent to (lambda a: a * 3)(11), which results in
# 11 * 3, giving us the output 33.



# try:
# # Code that may raise exceptions
# ...
# except (ExceptionType1, ExceptionType2, ...):
# # Handle ExceptionType1 or ExceptionType2 or ...
# # Common handling code
#
#
# try:
# x = int(input("Enter a number: "))
# result = 10 / x
# except (ValueError, ZeroDivisionError):
# print("Invalid input or division by zero")



#-----------------------------------------------------------------
try:
     x = int(input("Enter a number: "))
     try:
        result = 10 / x
            print(f"Result: {result}")
     except ZeroDivisionError:
        print("Division by zero inside nested try block.")
except ValueError:
        print("Invalid input. Please enter a number.")
