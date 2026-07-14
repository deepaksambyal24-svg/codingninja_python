n = int(input())
num =1
while num <= n:
    if num % 2 == 0:    # no is even
        num+=1          # go to next natural number
        continue        # go to nearest loop

    print(num)
    num += 1