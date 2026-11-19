def checkMember(n):

    if n == 0:   # ✔ handle edge case
        return True

    second_last = 0
    last_number = 1

    while last_number <= n:
        if last_number == n:
            return True

        fib = second_last + last_number
        second_last = last_number
        last_number = fib

    return False