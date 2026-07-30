# count thedigit and add all the number to its count power
# eg 123   1**3 + 2**3 + 3**4 = if it is same number then it is armstrong number


def count_digit (n):
    count = 0
    while n > 0:
        count+=1
        n = n//10
    return count
print(count_digit(10))

def check_armstron(n):
    d=count_digit(n)
    sum = 0
    temp=n
    while n > 0:
        rem = n % 10
        sum =rem**d
        n=n//10
    return sum==n