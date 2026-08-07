# CONTROL FLOW STATEMENT ---> It changes normal flow of a program
# there are three types control transfer  statement

# 1) BREAK ---> stop the work completely at that point and get out of the loop
#  2) CONTINUE--> Skip a particular item and move to the next
#  3) PASS ---> do nothing here for now , it allow the program to continue



# BREAK
for n in range(1,11):
    print(n,end=' ')
    if n==5:
        break




# check passwords and stopwhen the correct password is correct
password_attempt=['admin','company','secure123','test123']
correct_password='secure123'
for i in password_attempt:
    if i in correct_password:
        print('checked',i)
        if i==correct_password:
            print("login successful")
            break


transaction=['txn1','txn2','txn3','txn4','txn5']
suspicious_txn='txn3'
for t in transaction:
    print(t,end=' ')
    if t==suspicious_txn:
        print('found suspicious txn')
        break


# while loop with break ----> an ATM allows repeated until the daily limit of 2000 is reached
 # add each withdrawl and stop when the limit is reached

 # 1 starting point
 # 2 condition
 # 3 update

total_withdrawl=0
while True:
     total_withdrawl+=5000
     print(total_withdrawl,end=' ')
     if total_withdrawl==20000:
         print('daily withdrawl limit reached')
         break


# nested loop with break
# an airline checks seats row by row it wants to find the first available seat
# stop checking seats in the current row after an available seat in found
seat_rows =[["booked",'booked','booked'],['booked','available','booked'],['available','booked','booked'],['booked','booked','booked']]


for row_number,row in enumerate(seat_rows,start=1):
    for seat_number,seat_status in enumerate(row,start=1):
        if seat_status=='available':
            print('available seat found at row number',row_number,'seat',seat_number)
            break


# CONTINUE ----> Skip the current loop iteration  and move to the next iteration /cycle


for n in range (1,11):
    if n==6:
        continue
    print(n,end=' ')

# an ecom has some orders .canceled orders should not be considered
# skip orders whose status is cancelled
order_status=['confirmed','cancelled','confirmed','cancelled']
for i in order_status:
    if i=='cancelled':
        continue
    print('order sent for packaging ',i)


# we are checking the quality of all products out of 100
# only the products who have secured at least 70 should  be approved and considered

quality_ofProducts=[10,30,70,90,100,50,60]
for product in quality_ofProducts:
    if product>=70 :
        continue
    else:
        print("product qualify the quality check ",product)


# PASS ----> It does nothing on eg -->
for n in range(1,11):
    if n==6:
        pass
    print(n)

# order processing system with some  ruled :
# 1. stop the complete process when a fraud order is found
# 2. skip canelled orders
# 3 keep premium order login unfinished for now
# 4 process all other valid order s
orders =[{'id':'0101','status':'confirmed','type':'regular'},
         {'id':'0102','status':'confirmed','type':'premium'} ,
         {'id':'0103','status':'confirmed','type':'regular'},
         {'id':'0104','status':'confirmed','type':'regular'},]
for o in orders:
    if orders['status']=='confirmed':
        print("fraud found in ",o['id'])
        print("order processing stopped ")
        break
    if o ['status']=='cancelled':
        print('canceled orders skipped',o['id'])
        continue
    if o ['status']=='premium':
        pass
    print()


#      BREAK                                CONTINUE                                            PASS
#      stops the complete loop              no                                                   no
#    does not skip the current cyole        yes                                                     no
# impacts the flow                          yes                                                 does nothing



# an ed tech company is processing student applications for DA course follows certain rules :
#1  if the seats become full ,stop the processing  applications
#2   if a student has not paid the fee , disregards him /her
# 3 if a student belongs to the scholarship category ,the scholarship checking process is not ready yet ,
# then let it go as it is
#   all other eligible students are enrolled


seats =10
student_data=[{'student_id':'0101','name':'deep','fees_status':'paid','scholarship':'yes'},
              {'student_id':'0102','name':'jim','fees_status':'not_paid','scholarship':'no'},
              {'student_id':'0103','name':'adam ','fees_status':'paid','scholarship':'yes'},]

while seats<=10:
    for o in student_data:
        if o['fees_status']=='not_paid':
            break
        if ['scholarship']=='yes':
            print('scholarship process is not ready')
            continue
        seats-=1
    print()