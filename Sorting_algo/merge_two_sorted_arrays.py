#li = [1,2,3,4,6,9]
#l2=[3,8,9,10]
#merge both list in new list
def merege (l1,l2):
    i=0
    j=0
    n=len(l1)
    m=len(l2)
    l3=[]
    while i<n and j<m:
        if l1[i]<l2[j]:
            l3.append(l1[i])
        else:
            l3.append(l2[j])
            j+=1
    #may be l1 was exhausted byt l2 has elements
    while j <m:
        l3.append(l2[j])
        j+=1
        #may be l2 was exhauseted but l1 has lelement
    while i<n:
        l3.append(l1[i])
        i+=1
        