# Write your code here

string=input()
result=""
for ch in string:
    if ch in 'aeiouAEIOU':
        ch='x'
        result+='x'
    else:
       result+=ch
print(result[::-1])
