# data type
'''INT integer
TEXT string str
FLOAT decimal number
BOOLEAN boolean
DATE    '''

x=bool(1)# zero become false and 1 is true
print(x)  # and empty values are  also false type
print(bool(""))
print(bool("on"))


# checking the datatype
print(type(x))

# type conversion -known as typecasting
x=5
y=float(x)
print(x)
print(type(y))
#####
a=10
b =str(a)
print(a)
print(type(b))
# x=int(input("Enter a number:")) default data type of input function is string

#operator - is a symbol that allows to perform action on tow variable there are seven category of
# operator 7 types
# -arithmetic -->            - + % **
# comparison-->              ==,!=, < > <=, >=
# logical-->                 AND , OR , NOT
# bitwise-->                 & , ^ , ~ , << , >>
# assignment-->             =, -= , +=, ETC
# membership -->            IN , NOT IN
# identity  -->             IS , IS NOT


#ARITHMETIC  - modulo % gives the remainder and // floor division  ie quotient part

is_raining=True
print(not is_raining)

 # assignment membership
print( 'a' in 'Apple')  # it give me false because member ship are case sensitive
print('z' not in 'Apple')

# identity operator
x=4
y=5
print(x is y)

# bitwise
# AND  & --> both bits should be 1
#  OR  | -->  OR  Atleast 1 bit should be 1
# XOR ^ --> XOR  bits should be different
# NOT ~ --> not ( reverse bits)
# LEFT SHIFT <<  --> left shift  ( nultiply by 2
# RIGHT SHIFT >> --> right shift   divide by 2
x=8
y=10
print(bin(x))  # give binare ignore first two digit
print(bin(y))
print( x & y)
print( x | y)
print( x ^ y)
resutl=divmod(17.3)
print(resutl) # it gies the quotient and remainder as output
round(12.3444,2)
num1=7
num2 =100
# constraits --> limitaiton
1<=num1<=100  and 1<num2<=100 #means nmber between 1 and  100