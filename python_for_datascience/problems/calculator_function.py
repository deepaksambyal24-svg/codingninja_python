# Complete the function calculator


def calculator(operation, *args):
    # 1. Add : 10 + 2 + 3 + 14 = 29
    # 2. Subtract : 10 - 2 - 3 - 5 = 0
    # 3. Multiply : 3 * 2 * 2 = 12

    if len(args) > 1:

        def subtract(*args):

            res = args[0]
            for i in range(1, len(args)):
                res -= args[i]
            return res

        def add(*args):
            sum = 0
            for i in args:
                sum += i
            return sum

        def multiply(*args):
            res = 1
            for i in args:
                res *= i
            return res

        if operation == "add":
            res = add(*args)
            return res


        elif operation == "subtract":
            sub = subtract(*args)
            return sub
        elif operation == 'multiply':
            multi = multiply(*args)
            return multi
        else:
            return ('Invalid operation')
    else:
        return args[0]
