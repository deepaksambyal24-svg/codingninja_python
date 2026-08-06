# Function for armstrong number
def is_armstrong(n):
    sum = 0
    num = list(map(int, str(n)))
    for digit in num:
        sum += int(digit) ** len(num)
    if sum == n:
        return  print(f' Is {n} Armstrong number? {True}')
    else:
        return print(f' Is {n} Armstrong number? {True}')







is_armstrong(157)