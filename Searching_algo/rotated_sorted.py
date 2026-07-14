def find_in_sorted_rotated(li,target):
    #define search space
    start=0
    end = len(li)-1
    while start<=end:
        mid = (start+end)//2
        if li[mid]==target:
            return mid
        #decide if mid is on upper curve or lower curve
        if li[start]>=li[mid]:
            if li[mid]<=target<=li[end]:
                #discard left part
                start=mid+1
            else:
                #discard right
                end=mid-1
        else:
            if li[start]<=target<=li[end]:
                start=mid-1
            else:
                start=mid+1
    return -1