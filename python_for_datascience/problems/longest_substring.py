string = input()

empty_string = ""
pointer = 0
count = 0

for ch in string:
    while ch in empty_string:
        empty_string = empty_string[1:]
        pointer += 1

    empty_string += ch

    if len(empty_string) > count:
        count = len(empty_string)

print(count)