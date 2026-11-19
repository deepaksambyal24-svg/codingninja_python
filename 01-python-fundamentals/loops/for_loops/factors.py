n = int(input())
is_prime= True
for i in range(2,n):
    if n %i == 0:
        print(i,end=" ")
        is_prime= False
if is_prime:
    print("-1")