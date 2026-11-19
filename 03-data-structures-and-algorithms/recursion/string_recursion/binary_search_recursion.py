def binary_search_recursion(a,x,si,ei):
    if si>ei:     # base case
        return -1
    mid = (si+ei)//2   #Pmi
    if a[mid] == x:             #induction hypothesis
        return mid
    elif a[mid]  >x:
        return binary_search_recursion(a,x,si,mid-1)
    else:
        return binary_search_recursion(a,x,si,mid+1)
