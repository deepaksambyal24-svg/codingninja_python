def print_n(n):
    if n==0:
        return
    print_n(n-1)  # induction hypothesis
    print(n)
    return
n = int(input())
print_n(n)

# PRINT N TO 1
def print_n_to_1(n):
    if n==0:
        return
    print_n_to_1(n)
    print_n_to_1(n-1)
    