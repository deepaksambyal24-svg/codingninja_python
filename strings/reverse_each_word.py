def reverse_string(sentence):
    words=sentence.split()
    result=""
    for word in words:
        result+=word[::-1]+ " "
        result += " "
    return result.strip()
my="welcome to coding ninjas"
print(reverse_string(my))
