def first_index(arr,x):
    l=len(arr)
    if arr[0]==x:
        return 0
    if l==0:
        return -1
    smalloutput=first_index(arr[1:],x)
    if smalloutput==-1:
        return -1
    return smalloutput +1