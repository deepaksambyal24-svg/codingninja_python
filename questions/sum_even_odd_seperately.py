n=int(input())
even_sum=0
odd_sum=0

while n>0:
    rem = n % 10
    if rem % 2 == 0:
        even_sum += rem
    else:
        odd_sum += rem
    n = n // 10
print(even_sum,odd_sum)