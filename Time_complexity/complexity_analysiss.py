def sum_of_n_number(n):
    result =0
    for i in range(1,n+1):
        result += i
    return result


def sum_of_natural_n_optimized(n):
    return ((n)*(n+1)) //2     #WE HAVE ONLY THREE INSTRUCTION

