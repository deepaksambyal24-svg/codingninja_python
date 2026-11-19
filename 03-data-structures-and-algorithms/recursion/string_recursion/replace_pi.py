from Two_dimension_lists.list_comprehension import ele


def replace_pi(s):
    if len(s) == 1 or len(s) == 0:
        return s
    if s[0] =='p' and s[1] == 'i':
        smallouput=replace_pi(s[2:])

        return "3.14" + smallouput
    else:
        smallouput=replace_pi(s[1:])
        return s[0] + smallouput
    