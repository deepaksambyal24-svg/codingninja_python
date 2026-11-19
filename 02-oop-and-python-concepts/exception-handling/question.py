# Rishabh has recently learnt about custom exceptions. His friend gave him a task to initialise the salary with 500 in a class and raise an exception with message as "Insufficent funds in the account" if the withdrawl amount is greater than the bank balance otherwise display a message as " Remaining:remaining balance"
#

# Sample Input 1
# 400
# Sample output 1
#  Remaining:100
# Sample Input 1
# 600
# Sample output 1
# Insufficient funds in the account.





class my_exception(Exception):
    def __init__(self, balance):
        self.balance = balance


balance = 500
withdraw = int(input())

try:
    if withdraw > balance:
        raise my_exception(balance)
    else:
        print("Remaining:" + str(balance - withdraw))

except my_exception:
    print("Insufficient funds in the account.")