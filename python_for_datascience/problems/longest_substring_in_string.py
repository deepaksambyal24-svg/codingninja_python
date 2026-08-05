string=input()
ch1=1
empty_string=''
for ch in string:
    if ch not in empty_string:
        empty_string+=ch
print(empty_string)
