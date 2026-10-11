import math

def prime_factors(n: int) -> list:

     i=2
     num=n
     lit=[]
     if n>1:
            lit.append(num)
     else:
            while i < n:
                if num%i==0:
                    lit.append(i)
                    num= num//i
                else:
                    i+=1
            return lit