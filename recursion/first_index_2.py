def first_index(a,x,si):
    l = len(a)
    if si == l:
        return -1
    if a[si] == x:  #
        return si
    smallerlistoutput= first_index(a,x,si+1)
    return smallerlistoutput