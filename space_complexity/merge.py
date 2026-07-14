def merge(a,b):
    m=len(a)
    n=len(b)
    c=[]        # resultant list
    i=0         #iterate on list a
    j=0         #iterate on list b
    while i<m and j<n:
        if a[i]<b[j]:
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
    # if a has been exhausted , so probably b has some elements
    while j<n:
        c.append(b[j])
        j=j+1
    #if b is exhaustd, so probably a has some elemnts
    while i<m:
        c.append(a[i])
        i=i+1
    return c
print(merge([1,3,7],[2,5,8,9]))
