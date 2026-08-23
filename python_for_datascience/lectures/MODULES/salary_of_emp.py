import payrole_module
from python_for_datascience.lectures.MODULES.payrole_module import calculate_bonus

emp_sal =payrole_module.calculate_bonus(10000,0.1)
print(f"employee salary: {emp_sal:.2f}")

#*****************************************************************************************************************
# SOME COMMON IMPORT STYLES
#   1) IMPORT ENTIRE MODULE :- syntax is :  import    <module name>
#   2) IMPORT SPECIFIC FUNCTION OR CLASS FROM MODULE :- syntax is :  from <module name> import <function name>
#   3) IMPORT MULTIPLE FUNCTIONS : - syntax is :
#           from <module name> import <function name1>,<function name2>,<function name3>

#    4) IMPORT ALL FUNCTIONS FROM MODULE :- syntax is :  from <module name> import *


#*****************************************************************************************************************
