def isSorted(a):
    l= len(a)
    if l==0 or l==1:
        return True
    if a[0]>a[1]:
        return False
    smallerList=a[1:]
    isSmallerListSorted = isSorted(a[1:])
    if isSmallerListSorted:
        return True
    else:
        return False