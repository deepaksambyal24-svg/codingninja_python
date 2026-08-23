# Write your code here
num1 = input()
num2 = input()


def calculator(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2
    if num1 > num2:
        diff = num1 - num2
    else:
        diff = num2 - num1
    product = num1 * num2

    division = num1 / num2
    return sum, diff, product, division


calculator(num1, num2)

