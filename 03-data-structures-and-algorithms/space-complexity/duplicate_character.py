def calc_ways(i,j,m,n):
#base case
    if i ==m-1 and j ==n-1:
             return 1
    if i>=m or j >= n:
         return 0
    return calc_ways(i,j+1,m,n)+calc_ways(i+1,j,m,n)