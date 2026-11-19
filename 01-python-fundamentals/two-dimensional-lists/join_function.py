a='AB'.join('abcd')
print(a)
li ='av'.join(["1","2","3","4"])
print(li)


#2nd method
li= [[1,2,3],[4,5,6]]
n=3
for rows in li:
    outpu=' '.join([str(ele) for ele in rows])
    print(outpu)
