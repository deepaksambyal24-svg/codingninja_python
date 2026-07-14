nums=[1,2,3,4,5,6]
nums2  =nums[1:len(nums)-1]
nums3 =nums[1:-2]    # same as the above
nums4 =nums[:-3]   # only gives the last elemnt by leave the first element blank
print(nums2)
# [i:j]-> slice of element (i,i+1.....j-1)