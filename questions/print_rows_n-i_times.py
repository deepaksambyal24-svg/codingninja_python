def print_2d(arr,n,m):
   for i in range (n):
       for j in range (m):
           for k in range (n-i):
               print(arr[i][i],end=" ")
           print()
