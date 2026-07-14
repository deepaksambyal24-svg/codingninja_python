def merge(arr,left,mid,right,temp):
    i=left
    j=mid+1
    k=left
    count=0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            i=i+1
            k=k+1
        else:
            #count inversion
            count+=(mid-i+1)
            temp[k]=arr[j]
            j=j+1
            k=k+1
    while i<=mid:
        temp[k]=arr[i]
        i=i+1
        k=k+1
    while j<=right:
        temp[k]=arr[j]
        j=j+1
        k=k+1
        #transfer all the elements of temp back in arr
    for v in range(left,right+1):
        arr[v]=temp[v]
    return count
def helper(arr,temp,left,right):
    count=0
    if left<right:
        mid = (left+right)//2
        count+=helper(arr,temp,left,mid)
        count+=helper(arr,temp,mid+1,right)
        count+=merge(arr,left,mid,right,temp)
    return count


def mergesort(arr):
     temp=[0]*(len(arr))
     return helper(arr,temp,0,len(arr)-1)

def inversion_count(arr):
    pass
