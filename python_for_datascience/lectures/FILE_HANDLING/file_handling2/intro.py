import os
from _pyrepl import readline

from array.list.removing import remove

# reading data form files
# read () method or function
file=open('sales.txt','r')
content=file.read()  # it reads every thing from the file
print(content)
file.close()


# read(n) ---- eg first 3 char not everything some part of data

file = open('sales.txt','r')
print(file.read(7))
file.close()

# realline() --- real the lines from a file line by line

file = open('sales.txt','r')
first=file.readline()
second=file.readline()
print(first)
print(second)


# /n ---new line
print("apple\nbanana\norange")  # escape character

# readlines()   ----it return the list of list
file=open('sales.txt','r')
sales=file.readlines()
print(sales)
file.close()

''' READ reads everything and stores it in a variable  result is one sting 
REALLINE reads one line at a time    one stirng
READLINES reads all the lines separately    output is in for of list
FOR  process each line one by on e    one line per iteration '''



file=open('sales.txt','r')

# LOOPING THROUGH A FILE

# count customer complaints form camplaints from complaints.txt file

file =open('complaints.txt','r')
complaints=file.readlines()
print(f' total complaints : {len(complaints)}')


# read the first transaction
file =open('transaction.txt','r')
first_txn=file.readline()
print('first txn : ',first_txn)
file.close()


# find high value sales from a file  > 50000

file=open('orders.txt','r')
for o in file:
    product,amount=o.strip().split(',')
    amount=int(amount)
    if amount>50000 :
        print(f'{product} : ${amount}')
file.close()

# closing file  using exception handling
file =open('orders.txt','r')

try:
    content=file.read()
    print(content)
finally:
    file.close()

#
try:
    file=open('order.txt','r')          # file not exists
    try:
        content=file.read()
        print(content)
    finally:
        file.close()
except FileNotFoundError:
    print("File not found")



# safely read transaction logs
try:
    with open('employee2.txt','r') as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

# find pending shipment form shipments .txt file

try:
   with open ('shipments.txt','r') as file:
       for shipment in file:
           id,city,status=shipment.strip().split(',')
           if status=='pending':
               print(id,status)
except FileNotFoundError:
    print("File not found")


# writing data to a file
# create a daily sales report



# add text to a blank file
total_sales =875000
total_orders=425
with open('daily_sales_report.txt','w') as file:
    file.write('DAILY SALES REPORT\n')
    file.write('_____________________________\n')
    file.write(f'total_sales : {total_sales}\n')
    file.write(f'total_orders : {total_orders}\n')


# append new data in sales report
complaint1='customer101 gone wrong product'
with open('daily_sales_report.txt','a') as file:
    file.write('DAILY SALES REPORT new entry\n')
    file.write('_____________________________\n')
    file.write(f'''complaint1 : {complaint1}\n''')
    file.write(complaint1+'\n')

# create files checking files if exists
# check a file whether exists or not

try:
    with open ('checkingfiles.txt',"x") as file:
        file.write('salary report 2026 for all employees\n')
except FileExistsError:
    print("Report already exists")


year=2026
filename=f'financial_report_{year}.txt'
try:
        with open(filename,'x') as file:

            file.write('salary report 2026 for all employees\n')
            file.write('_____________________________\n')
            file.write('revneue:30000\n')
            file.write(f'PROFIT: 55500\n')
        print('report created successfully')
except FileExistsError:
    print('annual report already exists')


# daily branch report

branches =['mumbai','delhi','pune']
for b in branches:
    filename=b+'_daily_report.txt'
    try:
        with open(filename,'x') as file:
            file.write(f'salary report for site {b} for all employees\n')
            print(filename,'created successfully')
    except FileExistsError:
        print('annual report already exists')

# for deleting the file

import os


os.remove('mumbai_daily_report.txt')        # will remove the file


# use try block

try  :
    os.remove('mumbai_daily_report.txt')
    print('removed successfully')
except FileNotFoundError:
    print('file already deleted')


# other cases handling the permission eror

filename='temporary_sales_report.txt'
try:
    os.remove(filename)
    print('removed successfully')
except FileNotFoundError:
    print('file not deleted')
except PermissionError:
    print('permission denied')
