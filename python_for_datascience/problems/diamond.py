n = int(input())

# Upper Half
i = 1
while i <= n:
    space = 1
    while space <= n - i:
        print(" ", end="")
        space += 1

    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1

    print()
    i += 1


# Lower Half
i1 = 1
while i1 <= n - 1:
    space1 = 1
    while space1 <= i1:
        print(" ", end="")
        space1 += 1

    j1 = 1
    while j1 <= n - i1:
        print(n - i1, end=" ")
        j1 += 1

    print()
    i1 += 1