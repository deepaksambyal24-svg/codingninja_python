# FILE HANDLING ---> A process to handle manage files in the system with python code
# syntax  openfile ---> action---> close file
import os

# open ()   funtion ----> file object =open(filename,mode)

# DIFFERENT TYPE OF MODES
# 1) "r"----> read
# 2)  "w"---> write
# 3) "a" --> append
# 4)  "x"--> create

files=os.listdir()
for file in files:
    print(file)
file=open('file.txt','r')
content=file.read()
print(content)
file.close()

file=open('file.txt','w')
content=file.write('new contenct added')
print(content)
file.close()

file=open('file.txt','a')
file.write('/n  new content added')
file.close()

# file=open("new_file.txt","x")
# content=file.read()
# print(content)
# file.close()


# with open----.
with open("sales_aug.ext",'r') as file:
        data=file.read()
print(data)


#daily sales report
revenue=125000
orders=320
returns =12

with open("new_program.txt",'w') as file:
    file.write("daily sales report\n")
    file.write(f'revenue:{revenue}\n')
    file.write(f'orders:{orders}\n')

# store customer complaint log
customer='c101'
complaint='order delivered '
with open("new_program.txt",'a') as file:
    file.write(f'customer:{customer}\n')
    file.write(f'complaint:{complaint}\n')



# every day the ecom company wants python to calculate revenue and profit and gernate today's date
# create a folder for the reports ,create a report file  then save the data

from datetime import datetime
from module_business import *
qty=500
price=300
cost=110000
revenue=calculate_revenue(price,qty)
print(revenue)
profit=calculate_profit(cost,qty)
print(profit)
margin=calculate_margin(cost,qty)
print(margin)
today=datetime.now().strftime('%Y-%m-%d')
folder="daily_reports"
if not os.path.exists(folder):
    os.makedirs(folder)
file_name=f'{folder}/report_{today}.txt'
with open(file_name,'w') as file:
    file.write("daily business report\n")
    file.write(f'date:{today}\n')
    file.write(f'profit:{profit}\n')
    file.write(f'cost:{cost}\n')
    file.write(f'revenue:{revenue}\n')
    file.write(f'margin:{margin}\n')
print("file created")
