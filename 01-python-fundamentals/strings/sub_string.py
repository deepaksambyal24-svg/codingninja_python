def print_substring(inp):
    for start in range (0,len(inp)):
        for end in range (start ,len(inp)):
#             print(start,end)
# print_substring("abcd")
            s=""
            # for k in range (start,end+1):
            #     s+= inp[k]
            # print(s)
            s=inp[start:end+1]
            print(s)
print_substring("abcd")