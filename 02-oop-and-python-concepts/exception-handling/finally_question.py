def abc(x,y):
    try:
        res = x // y
        print(res)

    except ZeroDivisionError:
        print("Division not possible")

    finally:
        print("Program Exit")

x = int(input())
y = int(input())
abc(x,y)

# Problem statement
# Rishabh has recently learned about exception handling in Python. His teacher gave him a task to take two integer inputs from the user and print the result of their division.
#
#
# 
# The output should follow these conditions:
# 1. If the division is successful, print the result of the division, followed by the message "Program Exit" on the next line.
# 2. If the division is not possible (e.g., dividing by zero), print "Division not possible" followed by "Program Exit" on the next line.