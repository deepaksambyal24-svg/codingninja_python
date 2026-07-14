def fib(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    fib_1 = fib(n-1)
    fib_2 = fib(n-2)

    fib_num = fib_1 + fib_2

    return fib_num

print(fib(41))
import sys
sys.setrecursionlimit(100000)