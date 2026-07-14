def binary_search(li,target):
     n = len(li)
     start = 0
     end = n-1
     while start<=end:
         mid = (start+end)//2
         if li[mid]==target:
             return mid
         elif li[mid]<target:
             start=mid+1
         else:
             end=mid-1
     return None




