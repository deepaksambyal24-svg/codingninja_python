# if in place of printing the output of function we want to store the value of function in variable
def paymentdetails(name,age,phone,state):
    print("nameis ", name, "age is ", age, "phone is ", phone, "state is ",state)
    return ("upi","credit card")
    print("one more code to print") # it will never execute called as dead code




storing_variable= paymentdetails("deepak",39,89898,"hp")
print(storing_variable)

# the moment when return keyword it end the function
#no code will be execute after the retrun keyword
#you can return multiple value form code by using commas
paymentoption1,paymentoption2=paymentdetails("deepak",39,89898,"hp")
