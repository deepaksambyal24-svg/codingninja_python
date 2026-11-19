def user_billing_details(name,address,phone):
    print ("name",name,"address",address,"phone",phone)
def payment_detail(name,address,phone):
    #calling billing details
    user_billing_details(name,address,phone)
    return "credit card"
pay = payment_detail("","","123456")
    print (pay)