# we are using swaping in this algo so extra spaces or copy of arr are required
def  partition(a,si,ei):
    pivot= a[si]
    c=0
    #find number of elements smaller than pivot
    for i in range (si,ei+1):
        if a[i]<pivot:
            c+=1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index= si+c
    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i+=1
        elif a[j]>=pivot:
            j-=1
        else:
            a[i],a[j]=a[j],a[i]
            j-=1
            i+=1
    return pivot_index


def quickSort(a,si,ei):             # a=[10,9,8,7,1,3,5,,2]  # quick_sort[a,0,len(a)-1)

   if si >=ei:   #BASE CASE
        return
   pivot_index= partition(a,si,ei)
   quickSort(a,si,pivot_index-1)   # sort ist half
   quickSort(a,pivot_index+1,ei)    #sort 2nd half


a=[6,10,9,8,7,1,3,5,4,2]

quickSort(a,0,len(a)-1)
print(a)



