# mid // n is used for row no and mid %n for column no for 2d arrays
# to calculate end =((m x n) -1)
def find_in_2d(grid,target):
    m =len(grid)
    n = len(grid[0])
    start=0
    end = n*m-1
    while start<=end:
        mid= start + (end-start)//2
        row = mid//n
        col = mid%n
        ele = grid[row][col]
        if ele==target:
            return True
        if ele<target:
            start=mid+1
        else:
            end=mid-1
    return False