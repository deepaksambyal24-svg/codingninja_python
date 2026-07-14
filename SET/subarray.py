#subarray is contiguous cross-section of  a list
# sum (i,j ) = p(0,j) - p ( 0,i-1)
# so for  0 = p (0,j)-p(0,i-1)
# p(0,i-1) = p(0,j)
#eg   [1,2,3,5,-5,6]  prefix sum is [ 1,3,6,1,7}


# code


def check_subarray_withsum_zero(li):
    if len(li) == 0:
        return False
    else:
        s={li[0]}
        prefix_sum=li[0]
        for i in range(1,len(li)):
            prefix_sum+= li[i]
            if prefix_sum in s or prefix_sum==0:
                return True
            s.add(prefix_sum)
        return False