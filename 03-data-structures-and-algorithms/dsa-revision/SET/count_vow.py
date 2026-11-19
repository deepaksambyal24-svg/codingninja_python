def count_vow():
    string=input()
    for char in string:
        count=0
        if char in 'aeiou':
            count+=1
    print(count)
count_vow()