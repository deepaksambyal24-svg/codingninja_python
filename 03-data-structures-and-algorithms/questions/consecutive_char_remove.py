def remove_consecutive_char(string):
    string=""
    for i in range (1,len(string)):
        if string[i] == string[i-1]:
            string+=string[i]
        else:
            string+=string[i]
    return string
print(remove_consecutive_char("abcddddd"))