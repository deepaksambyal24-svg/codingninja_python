# MODULES ---> I
#    1) IT ALLOWS TO USE A PROGRAM IN MANY OTHER FILES INSTEAD OF THE SAME FILE WHERE IT IS CREATED
#    2) THE LINES OF CODE OF A PROGRAM CAN BE USED OR EASILY BE ORGANIZED IN DIFFERENT FILES
#    AND THEN IMPORTED IN THE MAIN FILE WHERE IT IS NEEDED
#   3) IT IS A FILE ENDING IN .py  AND IT CONTAINS REUSABLE PYTHON CODE  SUCH AS VARIABLES , FUNCTIONS , CLASSES
#       , CONSTANTS
import pricing
final_price=pricing.discounted_price(2000,15)
print(f'final_price:{final_price:.2f}')


# how to rename a module , we will use alias which is a temporary name inside the program

# syntax : --- import arith as arithmetic

# alias are optional and used when module name is long and short name or alternate is easily understood , two import
# names might conflict

# USE ALIAS FOR A FUNCTION  : SYNTAX IS ----> from arith import square as sq 