def removeConsecutiveDuplicates(string):

    if len(string) == 0 or len(string) == 1:
        return string

    smalloutput = removeConsecutiveDuplicates(string[1:])

    if string[0] == smalloutput[0]:
        return smalloutput

    else:
        return string[0] + smalloutput


# Main
string = input().strip()

print(removeConsecutiveDuplicates(string))