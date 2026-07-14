# find the pair for a element of x whose sum is equal to x in a list

def pair_sum(arr,x):
    total=0
    for i in range (len(arr)):
        left=arr[i]
        number= x-left
        for j in range (i+1,len(arr)):
            if arr[j]==x:
                total+=1
    return total
pair_sum([1,2,3,4,5,6],7 )

