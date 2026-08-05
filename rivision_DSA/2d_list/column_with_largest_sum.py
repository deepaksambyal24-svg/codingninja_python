list=[[1,2,3],[4,5,6],[7,8,9]]
# len of list give the length of list and li[0] give me the length of columns


def lar_col_sum(list):
   n=len(list)
   m=len(list[0])
   max_sum=0
   max_col_index=-1
   for j in range(m):
       sum=0
       for i in range(n):
           sum+=list[i][j]
           if sum>max_sum:
               max_col_index=j
               max_sum=sum
   return max_col_index,max_sum







lar_col_index=lar_col_sum(list)