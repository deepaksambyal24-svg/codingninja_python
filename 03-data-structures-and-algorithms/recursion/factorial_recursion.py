def factorial_recursion(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursion(n-1)



def sum_n(n):
    if n==0:
        return 0
    else:
        small_output = n +sum_n(n-1)
        return small_output

n = int(input())
print(sum_n(n))
print(factorial_recursion(n))