def bubble_sort(li):
    n = len(li)  # length of the list
    #the below loop represents the iteration number for us

    is_sorted = False
    for i in range(1,n):
        for j in range(0,n-i):#  the range is [0,n-i-1] actually
            if li[j]>li[j+1]: # the adjacent element is smaller that current element

                li[j],li[j+1]=li[j+1],li[j]
                is_sorted = True

        if is_sorted== False:
            return   # it means the li is already sorted, no need to iterate further
