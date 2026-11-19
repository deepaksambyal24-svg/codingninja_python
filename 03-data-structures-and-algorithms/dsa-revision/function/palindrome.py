def reverse_number(num):
    res=0
    power_of_ten=1
    while num>0:
        x=num%10
        res=res*10+x
        num=num//10
    return res
def check_palindrome(num):
    reverse=reverse_number(num)
    if reverse==num:
        return True
    else:
        return False
if check_palindrome:
    print('palindrome')
else:
    print('not palindrome')
check_palindrome(12321)