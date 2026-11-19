def binary_search_self(arr,target):
    start =0
    end = len(arr)
    mid = (start+ end) //2
    while search>=0:
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]>target:
            end=mid-1
        elif arr[mid]<target:
            start=mid+1
    return None
