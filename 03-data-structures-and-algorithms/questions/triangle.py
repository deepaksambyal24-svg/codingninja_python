i = 1
n=int(input())
while i <= n:
    j = 1
    while j <= i - 1:
        print(" ", end="")

        j += 1
    # star
    k = n
    while k >= i:
        print("*", end="")
        k -= 1
    print()
    i += 1