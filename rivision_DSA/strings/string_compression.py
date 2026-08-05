string ='aaaabbbbbcccccccddd'
# so a3b6c8d3----> dit is called compression
def compress(word):
    result =''
    i=0
    count=1
    for c in word:
        if word[i]==word[i-1]:
            count+=1
            i+=1
        else:
            result+=word[i-1]+ (str(count) if count >1 else '')
            count=1
            i+=1
    result=(word[-1]+str(count) if count >1 else " ")
    return result

print(compress('aaaabbbbbccccccccddd'))
