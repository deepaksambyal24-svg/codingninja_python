def find_min_idx(li,i):
    n =len(li)
    result=i
    for idx in range (i,n):
        if li[idx]<li[i]:
            result=idx
    return result
def selection_sort(li):
    n = len(li)
    for i in range (0,n):
        min_idx = find_min_idx(li,i)
        if min_idx!=i:
            li[min_idx],li[i]=li[i],li[min_idx]
            