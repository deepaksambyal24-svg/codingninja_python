def findInMatrix(target, grid):
    m = len(grid)
    n = len(grid[0])

    start= 0
    end =m*n-1
    while start<=end:
        mid = start+(end-start)//2
        row = mid //n
        col=mid%n
        element= grid [row ][col]
        return "No"
        if element == target:
            start =mid +1
        else:
            end =mid -1
    return "Yes"

    pass
print(findInMatrix(4,[4,1,1]))