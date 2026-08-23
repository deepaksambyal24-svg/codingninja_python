item=input().split()

key=[]
value=[]
for both in item:
    if both.isdigit():
        key.append(int(both))

    else:
        value.append(both)
dic = {key: value for key, value in zip( value,key)}
print(dic)
