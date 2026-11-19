#question_--> given a list of numbers ,checkif there is a sublist /subarray whose element sum upto 0



# subarray ---->contiguous cross-section of a list


# if in the array there is an single occurrence of zero then answer is true

# concept ---> Prefix sum  arra=[1,2,3,4,5]
''' the prefix sum for p(i,j)= p(0,j) -p(0,i)
eg.------>    sum(2,4)  = p(0,4) - p(0,1)    == 15 -3 =12
'''


arr=[2,3,4,5,-6,-1,2,4,8]
# prefix sum = 2,5,9,14,8,7,9,13,21


# TO CALCULATE SUBARRAY SUM FORM (3,6) =P(0,6) -P(0,3) =9-9 =0



def check_subarray_with_sum_zero(li):
    if len(li)==0:
        return False
    if li[0]==0:
        return True
    s={li[0]}
    prefix_sum=li[0]
    for i in range(1,len(li)):
        prefix_sum += li[i]
        if prefix_sum in s:
            return True
        s.add(prefix_sum)
    return False