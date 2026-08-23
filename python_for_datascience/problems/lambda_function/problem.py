# lambda   INPUT : CALCULATION

#
#
#
#
# Imagine you have a big machine called a function. Usually, you give it a name:
# def square(x):
#     return x * x
# Then you use it:
# square(5)
# Output:
# 25
# But what if you need a very small function only once? Do you really want to give it a name and write several lines? 🤔
# That's where lambda comes in!
# 1. What is a Lambda Function?
# A lambda is a small, anonymous function.
# Anonymous simply means:
# "I don't need to give this function a name."
# Basic structure:
# lambda arguments: expression

lambda x: x*x
# this means take x and give me x**2
# LAMBDA AUTOMATICALLY RETURN THE VALUE SO WE DONT WRITE RETURN
# ALTHOUGH LAMBDA FUNCTION ARE ANONYMOUS WE CAN ASSIGN IT TO A VARIABLE
# LAMBDA CAN TAKE MULTIPLE PARAMETER BUT ONLY ONE EXPRESSION
#
def oneLineFunction():
    # Replace 'None' with one line function performing the required operations

    # Lambda Function to concating the string
    concat = None
    concat = lambda s1, s2: str(s1) + str(s2)

    # Lambda Function to Convert to Uppercase
    to_upper = None
    to_upper = lambda x: x.upper()

    # Lambda Function to Check if a String is Palindrome
    is_palindrome = None
    is_palindrome = lambda str: str == str[::-1]

    # Lambda Function to Get the Length of a String
    get_length = None
    get_length = lambda l: len(l)

    # Lambda Function to Replace Spaces with Underscores
    replace_spaces = None
    replace_spaces = lambda r: r.replace(" ", "_")

    # Lambda Function to Get Initials from a Full Name
    get_initials = None
    get_initials = lambda name: '.'.join([word[0] for word in name.split()]) + '.'

    # Lambda Function to Reverse a String
    reversed_string = None
    reversed_string = lambda s1: s1[::-1]

    # Don't make any changes to the return statement
    return (concat, to_upper, is_palindrome, get_length, replace_spaces, get_initials, reversed_string)
