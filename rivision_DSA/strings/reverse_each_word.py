word="this is a holiday in india"
each_word=word.split(' ')
result=''
for word in each_word:
    result+=word[::-1]
    result+=' '
print(result)