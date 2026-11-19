def check_palindrome(num):

    rev=num.copy()
    rev.reverse()
    return num==rev
print(check_palindrome([1,2,1]))

def check_palindrome2(num2):
    hi=len(num2)-1
    lo= 0
    while lo<=hi:
        if num2[lo]!=num2[hi]:
            return False
    return True
print(check_palindrome2([1,2,1]))