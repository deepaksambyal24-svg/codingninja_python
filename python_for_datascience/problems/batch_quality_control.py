from typing import List


def count_divisible(n: int, k: int, a: List[int]) -> int:
    # Write your code here
     count = 0
     li=list(map(int,  a.split()))
     for ele in li:
         if int(ele) % int(k)==0:
             count += 1
         else:
             continue
     return count





n=5
k=3
a=" 1 2 3 4 6"
print(count_divisible(n,k,a))