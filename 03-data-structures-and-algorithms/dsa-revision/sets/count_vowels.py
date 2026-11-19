string='how are you'
vowels=['a','e','i','o','u']
count=0
for i in string:
    if i in vowels:

        count=count+1
print(count)


def unique_vowels(string):
    result=[]
    