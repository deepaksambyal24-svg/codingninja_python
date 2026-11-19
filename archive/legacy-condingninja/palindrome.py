from typing import List
def palindrome(n: int) -> bool:
    number =0
    original =n
    while n>0:
        rem = n%10
        number =number*10 +rem
        n//=10
        if number== original:
            return True
        else:
            return False