#rearrange such that odd number are right and  even number at right
def arrange_into_even(arr):
    first_odd=0
    for i in range (len(arr)):
        if arr[i]%2==0:
            arr[i],arr[first_odd]=arr[first_odd],arr[i]
            first_odd+=1
    print(arr)
arr = [1,2,3,4,5,6]
arrange_into_even(arr)
