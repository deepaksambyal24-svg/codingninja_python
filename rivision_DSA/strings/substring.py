# substring ---> subsring is conteous cross section of the string


# problem is find the all possible substring of a given string
def print_substring(inp):
    for start in range(0,len(inp)):
        for end in range(start,len(inp)):
            s=' '
            for k in range(start,end+1):  # this loop is used to create a substring
                s=s+inp[k]
            print(s)


print_substring('abcd')




# second method using slicin
s = "abcd"
for start in range(len(s)):
    for end in range(start, len(s)):
        print(s[start:end+1])