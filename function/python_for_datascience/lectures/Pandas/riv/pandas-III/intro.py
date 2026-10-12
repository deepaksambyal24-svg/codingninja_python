# STATISTICAL OPERATION OF PANDAS ------.
import numpy as np
import pandas as pd
from pandas.core.dtypes import dtypes

purchases=pd.read_excel('purchases.xlsx')
products=pd.read_excel('products.xlsx')
customers=pd.read_excel('customers.xlsx')


print(purchases.mean(numeric_only=True))


# select only numeric columns

numeric_columns=purchases.select_dtypes(include=['number'])
print(numeric_columns.mean())
print(numeric_columns)

# mean of specific column


purchases['paid'] = purchases['paid'].str.replace(r'[$,]', '', regex=True) .astype(float)
print(purchases.dtypes)
print(purchases.mean(numeric_only=True))

#MEDIAN
print(purchases['paid'].median())

numeric_columns=purchases.select_dtypes(include=['number'])
print(numeric_columns.median())

# MODE
print(customers.mode())

# maximum values

max_values =purchases.max(numeric_only=True)
print(max_values)
max_val=max_values.astype(int)
print(max_val)

# sum of values
sum_value=purchases.sum(numeric_only=True)
print(sum_value)

# count of values in each column
column_counts=products.count()
print(column_counts)

# calculate the frequency analysis
# CALCULATE THE FREQUENCY DISTRIBUTION OF THE COMPANY COLUMN IN THE PRODUCTS DATAFRAME
company_counts =products['company'].value_counts()
print(company_counts)

gender_counts=customers['gender'].value_counts()
print(gender_counts)


# data aggregation

num=purchases.select_dtypes(include=['number'])
print(num.aggregate(['sum','min']))


# sorting a dataframe
sorted_purchases=purchases.sort_values(by='amount',ascending=False)
print(sorted_purchases)

sorted_products_mulit_de=products.sort_values(by=['company','cost'],ascending=[False,True])
print(sorted_products_mulit_de)

# idx max functionn    --> retrun the index  or label of the first occurrence of the maximum value

index_max_products=products.idxmax()
print(index_max_products)


index_max_paid=purchases['paid'].idxmax()
print(f'index of maximum paid amount:{index_max_paid}')


# group by functions  ----> grouping data based on one or more columns and then apply functions such as sum mean count to each group

# Grouping involves the following steps:
# ● Splitting: Data is divided into groups based on some criteria.
# ● Applying: A function is applied to each group independently.
#  Combining: Results are combined into a DataFrame, Series, or aggregated result

# group by 'company' column

# calculate average cost of products per company
products['cost']=products['cost'].str.replace(r'[$,]', '', regex=True).astype(float)
grouped_by_company=products.groupby('company')

# calculate the averag
average_cost=grouped_by_company['cost'].mean()

# calculate total number of products per company
total_products =grouped_by_company['product'].count()

#m display the result
# Display the results
print("Average Cost of Products per Company:\n", average_cost)
print("\nTotal Number of Products per Company:\n", total_products)


# Group by 'purch_date' and calculate the total 'paid' amount per date

total_paid_per_date=purchases.groupby('purch_date')['paid'] .sum()
#group by product_num and calculate the average 'amount' purchased per product

avg_amount_per_product=purchases.groupby('product_num')['amount'].mean()
# print the result

print("Total paid amount per date:")
print(total_paid_per_date)



# altering the index    --> rearrange the dataframe so that the specified column becones the index
customers.set_index('id',inplace=True)
print(customers)

# reset index
customers.reset_index(inplace=True)
print(customers)



