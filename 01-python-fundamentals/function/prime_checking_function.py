def check_prime(num):
    for n in range (2,num):
        if num % n == 0:
            return False
    return True
x= check_prime(17)
if x:
    print("Prime")
else:
    print("Not Prime")