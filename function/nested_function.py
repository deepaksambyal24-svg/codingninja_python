def user_billing_details(name,address,phone_number):
    print ( "nameis ", name,"address of the user is ", address ,"phone number is ", phone_number)


def payment_details(name,address,phone_number):
    #calling user billing function
    user_billing_details(name,address,phone_number)
    return "credit card","upi"
payment_option= payment_details("deekpak","39","8888888")
print(payment_option)