from turtledemo.chaos import line

import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
# Creating a figure and a plot
plt.plot(x, y,label='Prime Number',color='red')

# adding title and labels
plt.title('simple line plot ')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend()
plt.show()


#linewidth and line style
# Data
weight = [19.7, 21.3, 23.5, 25.9, 28.5, 32.1, 35.7, 39.6, 43.2]
height = [121.9, 124.5, 129.5, 134.6, 139.7, 147.3, 152.4, 157.5,
162.6]
# Plot settings
plt.figure(figsize=(8, 6)) # Adjust figure size if necessary
plt.plot(weight, height, color='green', marker='*', markersize=10,
linestyle='--', linewidth=2, label='Average Weight vs Height')
# Adding labels and title
plt.title('Average weight with respect to average height')
plt.xlabel('Weight in kg')
plt.ylabel('Height in cm')
# Display the grid
plt.grid(True)
# Adding legend
plt.legend()
# Show plot
plt.show()
# generate data using numpy arrays
import numpy as np
import matplotlib.pyplot as plt
# Generate data using NumPy arrays
x = np.array([0, 1, 2, 3, 4, 5])
y = x ** 2
# Create a plot using Matplotlib with specified marker, markersize, line style, and line width
plt.plot(x, y, marker='o', markersize=8, linestyle=':',
linewidth=2, color='#FF5733', label='Data Points')
# Customize plot
plt.title('Plot with Customizations')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid(True)
# Customize x and y ticks
plt.xticks(np.arange(0, 6, step=1)) # Custom x ticks from 0 to 5 with step size 1
plt.yticks(np.arange(0, 26, step=5)) # Custom y ticks from 0 to 25 with step size 5
# Display legend
plt.legend()
plt.show()


import pandas as pd
customers=pd.read_csv('Customers.csv')
products=pd.read_csv('Products.csv')
purchases=pd.read_csv('Purchase.csv')
print(customers)
print(products)
print(purchases)

print(products.isnull().sum())
gender_count=customers['gender'].value_counts()
print(gender_count)
plt.figure(figsize=(8, 6))
plt.pie(gender_count,labels=gender_count.index,autopct='%1.1f%%',startangle=140,colors=
        ['#1f77b4','#ff7f0e'])
plt.title('Gender distribution of customers')
plt.axis('equal')  # ensure the pie is drawn as a circle
plt.show()

# creating a bar chart
# calculate city wise customer counts
city_counts=customers['city'].value_counts().head(10)   # top 10

# plotting the bar chart
plt.figure(figsize=(8, 6))
city_counts.plot(kind='bar', stacked=True,color='#1f77b4')
plt.title('top 10 cities with highest customer count')
plt.xlabel('City')
plt.ylabel('Number of cities')
plt.xticks(rotation=45)
plt.show()


#ensure the purch_date column is the datetime format

print(purchases['purch_date'].dtype)
purchases['purch_date']=pd.to_datetime(purchases['purch_date'])
purchases['month']=purchases['purch_date'].dt.month

# group by month and sum the amount
spending_over_time_monthly=purchases.groupby('month')['amount'].sum().reset_index()

# plotting the line chart
plt.figure(figsize=(12,6))
plt.plot(spending_over_time_monthly['month'],
spending_over_time_monthly['amount'], marker='o', linestyle='-',
color='b')
# customize plot
plt.title('Total customer spending over time (monthly)',fontsize =16,fontweight='bold')
plt.xlabel('Month',fontsize =16,fontweight='bold')
plt.ylabel('total amount spent',fontsize =16,fontweight='bold')
plt.grid(True,linestyle='--',linewidth=.5)
plt.xticks(spending_over_time_monthly['month'])


# display the plot
plt.show ()


# group by company and calulate the average the cost
avg_cost_by_company=products.groupby('company')['cost'].mean().reset_index().head()

# sort the data by cost for better visualization

avg_cost_by_company=avg_cost_by_company.sort_values(by='cost',ascending=False)


# plotting the bar chart
plt.figure(figsize=(12,6))
plt.bar(avg_cost_by_company['company'],avg_cost_by_company['cost'])

# customize plot
plt.title('Average cost by company',fontsize =16,fontweight='bold')
plt.xlabel('Company',fontsize =16,fontweight='bold')
plt.ylabel('Average cost',fontsize =16,fontweight='bold')
plt.xticks(rotation=45)
plt.grid(axis='y',linestyle='--',linewidth=.5)

#display the plot
plt.show()


# create a boxplot of paid column
plt.figure(figsize=(12,6))
plt.boxplot(purchases['paid'])
#customize plo t
plt.title('boxplot of amount paid',fontsize =16,fontweight='bold')
plt.ylabel('Amount paid',fontsize =16,fontweight='bold')
plt.grid(True,linestyle='--',linewidth=.5)
# display the plo t
plt.show()


# to save the output in a particular format and location
plt.savefig('plot.png',format='png')


# regression plot ---> adding a regression line to a scatter plot
import seaborn as sns
