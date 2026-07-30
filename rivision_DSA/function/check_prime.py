def check_prime(num):
    for dev in range(2, num):
        if num % dev == 0:
            return False
    return True
result= check_prime(10)
if result:
    print("Prime")
else:
    print("Not Prime")
