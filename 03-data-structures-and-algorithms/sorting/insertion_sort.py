def insertion_sort(li):
    n = len(li)
    # intially left region [0] , right region [1,n-1]
    for i in range(1,n):
        # this loop i iterates on every element from index 1 to n-1
        # value at i should be now inserted at right position
        element = li[i]
        j = i-1
        while j>=0 and li[j] > element:
            li[j+1] = li[j]
            j-=1
            #right index to put value of ith index is j+1 th index
            li[j+1] = element
            