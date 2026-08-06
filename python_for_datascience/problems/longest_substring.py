string=input()
set_substring=set(string)

if len(string)==1:
    print(string)
else:
    longest_substring=""
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            substring=string[i:j]
            if len(substring)==len(set(substring)):
                if len(substring)>len(longest_substring):
                    longest_substring=substring
    print(longest_substring)