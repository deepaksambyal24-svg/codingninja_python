def squareroot(num):
    start=1
    end = num
    ans =end
    while(start<=end):
        mid=(start+end)//2
        if mid*mid >=num:
            start=mid+1
            ans = mid
        else:
            end=mid-1
    return ans

