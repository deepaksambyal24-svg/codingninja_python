# string is a text data it is written inside the inverted commas ie quotes
'''strings can contain letters numbers spaces symbols and panctuatoin marks '''
#slicing,split,replace,concat,negative indexing ,len ,upper, strip

# INDEXING --> Means finding one specific character from a string using its position
#----------------------------------------------------------------------------------
# INDEX always start from zero
word ='python'
print(word[0]) #--> 'p'
#----------------------------------------------------------------------------------
# NEGATIVE INDEX --> from right to left
word = "python"
print(word[-1])
# and -6 for first character from left
a = 'hello world!'
print(a[-7]) # spaces are also considered as data
# ERROR -->
# INDEX ERROR if we searching any character 's position which doesnot exist
#----------------------------------------------------------------------------------
#SLICING--> Cutting the part of the string
# syntax --> start ,end ,step
word = "python"
print(word[1:4])
a='hello world!'
print(a[1:5:2])
print(a[1:])# include till end
print(a[:5])# all to the left from 5 th positioni

# for output el,wr
a='hello, world!'
print(a[1:10:2]) # O/P --> el,wr

b="ABCDEFG"
print(b[0:7:2]) ## oo/p --> ACEG

c="python programming is fun!"
print(c[-4:])  # o/p --> fun!

print(c[:-5])

print(c[::-1])  # reverse the string in reveral order
#----------------------------------------------------------------------------------
# len function --> count the number of character in a string
a='hi, there!'
print(len(a))
#----------------------------------------------------------------------------------

# UPPER --> convert character ot upper case
print(a.upper())  # --> uppercase
print(a.lower())   # --> lower case
print(a.title()) # --> sentence case
print(a.swapcase()) # --> swap the case
print(a.capitalize())  # --> only first chartacter capatilize
#----------------------------------------------------------------------------------
#concat --> joining text  + symbol used
b="date "
print(a+" "+ b)
c= 10
d ="john"
print(str(c)+" "+ d)
#----------------------------------------------------------------------------------
#repeating a string
print(a*3)
#----------------------------------------------------------------------------------
# comparing the strings
a="apple"
b="banana"
print(a==b)
print(a!=b)
print(a>b)
print(a<b) # because a comes prior than b
x="apple"
y="Apple"
print(x==y)
print(x!=y)
print(x>y) # capital letter are considered smaller than lower case  letter
print(x<y)
#----------------------------------------------------------------------------------
# REPLACE--> Strings are immutable but replace can be done by replace function
x="Hello, world!"
x.replace("Hello","Python")
print(x)
z=x.replace("o","x")
print(z)
#----------------------------------------------------------------------------------
# SPLIT--> breaks a string into parts and returns all the part as a list
a="This is a string"
print(a.split()) # it can take parameter for delimiter
b="the,second,depak"
print(b.split(",")) # "," is the parameter for delimiter it split the string based on this
#----------------------------------------------------------------------------------
# format () --> customize the look of ouput, place holders are empty
age=30
name="alex"
x="my name is {age} , i am {name} year old ".format(age=age,name=name)
print(x)

#----------------------------------------------------------------------------------
# f-string --> takes parameters inside the placeholder
b=f"my name is {age} , i am {name} year old "
print(b)
#----------------------------------------------------------------------------------
# strip() functin --> it remove extra spaces from the string beginning and end
z= " ddd   "
print(z.strip())
z="**helo**"
print(z.strip("*")) # remove from both side
print(z.lstrip("*"))  # remove from left side


string = "Hello"
print(string.strip('o')) #--> also used to remove char 
#----------------------------------------------------------------------------------
# INDEX
sentence ="this is a sentence"
index=sentence.index("is")
print(index)
#----------------------------------------------------------------------------------
 # find
index=sentence.find("is",3,10)
print(index) # this search is between the index 3 and 10 in the string  since is is found at index
# 5 so it returns 5
# find returns -1 if substring not found and no error raised
# index reaises value error and raise error

#----------------------------------------------------------------------------------
# start with()
print(sentence.startswith("this"))  # returns True and it is case sensitive
print(sentence.endswith("is"))
print(sentence.count("is",1,3))  # it accespt the parameter too

#----------------------------------------------------------------------------------
# count() is used to count occurance of a substing and return '0  if not found
count=sentence.count("ist")
print(count)  # return 2 as output

b="banana"
print(b.count("a"))  # return 03 as output

#----------------------------------------------------------------------------------

# isalpha() chech whether the substring only contains aplhabetic or consit of letter
# retrun False for if letter exist
text1="hello"
text2='hello123'
print(text1.isalpha())
print(text2.isalpha())
print(text1.isalnum())
print(text2.isalnum()) # isalnum() all characterare alphanumeric or not


#----------------------------------------------------------------------------------
# isupper()
a="HELLO123"
print(a) # return True --> because letter are not case sensitive as same for special char



#----------------------------------------------------------------------------------
#isnumeric() check whether all char are numerical or not
a=12345
print(a) # --> return true
#----------------------------------------------------------------------------------
# isalum()     it can combination of both alpha and num  no spaces and special char
# included

a="hellp123"
print(a.isalnum()) # is True -->
b="hello_123"
print(b.isalnum()) # False -->
#----------------------------------------------------------------------------------
#isdigit() to check the string are digits ornot
# same
print("123".isnumeric())
print("Ⅻ".isnumeric())    # Roman numeral for 12
print("½".isnumeric())     # Fraction all true this is differencce between
# isnumeric and isdigit



#----------------------------------------------------------------------------------
#split()

str1 = "Coding Ninjas"
a = str1.split(" ")  # --> it finds the space and then create a list
print(a)
