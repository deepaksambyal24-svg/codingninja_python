# CONTROL STATEMENT--> Not repeating same code  many times , easy bunding
# creating algorithms
from python_for_datascience.problems import print_input

# TYPES OF CONTROL STATEMENTS
#1. CONDITIONAL STATEMENTS
#2. LOOPING STATEMENTS
#3. CONTROL TRANSFER STATEMENTS

#--------------------------------------------------------------------------------#
# CONDITIONAL STATEMENT ---> it allows python to perform different actions depending on whether a condition met or not

# if  , if-else, if elif ,else

#IF ----> it executes a block of code only when condition is true
a=10
if a>5:
    print("mode")



# TRUTHY AND FALSY VALUES
# FALSY VALUES ---> 0,0.0 , ",{}, [],()
# TRYTHY VALUES --> 1, 'TYTHON', [1],{2,3},(1,2)


#-----------------------------------------------------------------------------------------------------#

# IF -ELSE ----->
customer=['aman','priya','rahul']
if customer:
    print("customer")
else :
    print("customer are not")



# example 2
a ='udip'
if "g" in a:
    print("found")
else :
    print("not found ")

a={'a':1,'b':2,'c':3   }
b={'d':4,'e':5,'f':6,'g':7}
c='z'
if c in a:
    print("found")
else :
    print("not found ")

#-------------------------------------------------------------------------------------------------------#
# IF ELIF ELSE : ----> More than two conditions
# labeling based on marks
marks = 30
if marks >=90:
    print('excellent')
elif  marks >=70:
    print('verygood')
elif marks >=40:
    print('excellent')
else:
    print('fail')


# logical opertors

age =30
income =50000
if age>=12 and income>=40000:
    print('target')
else :
    print('not target')


#-------------------------------------------------------------------------------------------------------------#
#NESTED CONDITIONAL STATEMENTS--> One conditonal statement within another  it is useful when the second decision should
# be made only after the first condition is satisfied

# appraisal feedback
performace_rating =4.5
yos =3
if performace_rating >=4 and performace_rating <=5:
    print('yes')
    if yos >=3:
        print('eligible')
    else:
        print('service')
else:
    print('not eligible')



i = 5
while True:
    if i%0o11 == 0:
        break
    print(i)
    i += 1


#   SHORT HAND If -----> when an if block contains only one simple statement .it may written on one line of code
# whether a person is an adult or not
if age >=18:
    print('you are an adult ')
# short hand
if age >=18: print("your are an adult ")     # short handed

# shorthand syntax for if else -------> value_if_true if condition else value_if_false

x=10
message="even" if x%2==0 else "odd"
print(message)



# problem ---> ecommerce dicount and final bill
actual_bill=0
bill =int(input("enter your bill"))
if bill>=500:
    actual_bill=bill-(bill*.2)
    print(actual_bill)
elif 300<=bill<=499:
    actual_bill=bill-(bill*.15 )
    print(actual_bill)
elif 150<=bill<=299:
    actual_bill=bill-(bill*.1 )
    print(actual_bill)
elif 500<=bill<=149:
    actual_bill=bill-(bill*.3)
    print(actual_bill)
else:
     print(bill)

 #------------------------------
 # employee performance bonus, company calculates the performance based on :
 # sales acheivement : 50%
 # customer rating : 30 %
 # attendance : 20 %
 # if score is >=90 ,bonus is 20 %
 # if score 89 89 bonus is 15 %
 # if score 70-79 bonus is 10 %
 # if score 60-69 ,bonus is 5 %
 # below 60 no bonus
  # if atendancec < 75 % , the employee is not eligible for bonus
monthly_salary=int(input("enter your monthly salary"))
sales_score =int(input("enter your sales score"))
customer_rating=int(input("enter your customer rating"))
attendance=int(input("enter your attendance % :"))
final_score = (sales_score*0.50+customer_rating*0.30+attendance*.20)
if attendance<75:
    bonus_rate=0
    performance_category="not eligible"
elif final_score>=90:
    bonus_rate=20
    performance_category="outstanding"
elif final_score>=80:
    bonus_rate=15
    performance_category="excellent"
elif final_score>=70:
    bonus_rate=10
    performance_category="good  "
elif final_score>=60:
    bonus_rate=5
    performance_category="satisfactory "
else:
    bonus_rate=0
bonus_amount=monthly_salary*bonus_rate/100
final_salary=monthly_salary+bonus_amount
print('\n------performance report -----------')
print('your monthly salary',monthly_salary)
print('your sales score',sales_score)
print('your customer rating',customer_rating)
print('your attendance',attendance)
print('your final salary',final_salary)
print('your performance',performance_category)
print('your bonus amount',bonus_amount)


#---------------------------------------------------------------------
# problem using nested if ------------------------>
# college scholarship assessment :
# a college grants scholorships based on :
# academic score ,finaly income , entranc score , sports participation
# basic eligibility ; at least 75 percent of attendance , no failed subjects , entrance score should be min 60
# sholarship rules : ----> academic score >=90 ,family income<=30000 scholarship will be 100
# academic score >=85 ,family income<=45000 scholarship will be 75
# academic score >=75,family income <=6000 shcolarship will be 50 %
# academic score >=70 scholarship will be 25 %
 # otherwise 0 %
 # a state level or national level sportperson reeives an additional 10 % , btu the total scholarship cannot exceed 100%

academic_score=int(input("enter your academic score"))
family_income=int(input("enter your family income"))
entrance_score=int(input("enter your entrance score"))
attendence=int(input("enter your attendance "))
failed_subject=int(input("enter your failed subject"))
sports_level=input("enter your sports level:none/distict/state//national:")


if attendence>=75:
    if failed_subject==0:
        if entrance_score>=60:
            if academic_score>=90 and family_income<=30000:
                scholarship_rate=100
            elif academic_score>=85 and family_income<=45000 :
                scholarship_rate=75
            elif scholarship_rate>=75 and family_income<=60000 :
                scholarship_rate=50
            elif academic_score>=70:
                scholarship_rate=25
            else:
                scholarship_rate=0
            if sports_level=="state" or sports_level=="national":
                scholarship_rate+=10
            if scholarship_rate>100:
                scholarship_rate=100
            annual_fee=12000
            scholarship_rate=annual_fee*scholarship_rate/100
            student_payment=annual_fee-scholarship_rate
            print("\n------scholarshipresult-----")
            print('scholarship percentage',scholarship_rate)
            print('scholarship percentage',scholarship_rate)
            print('annual fee',annual_fee)
            print('scholarship percentage',scholarship_rate)
        else:
            print('not elgible ')
    else:
        print('not eligible as there are failed subject')
else:
    print('not eligible because of below 75 % attedence')   