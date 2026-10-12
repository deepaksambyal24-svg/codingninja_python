import pandas as pd
cust=pd.read_csv('customers.csv')
pur=pd.read_csv('purchases.csv')
prod=pd.read_csv('products.csv')
print(cust.head())
print(pur.head())
print(prod.head())
# to_datetime - Used to convert a column to datetime format. From a datetime column, you can extract parts like month (dt.month) and year (dt.year).
#
# astype - Used to convert a column from one data type to another, for example from string to float.
#
# str.replace with regex - Used to remove special characters like the dollar symbol from a column before converting it to a numeric type. regex=True is used to apply the regular expression pattern.
#
# isna / isnull with sum - Used to identify and count missing values in each column of a table.
#
# fillna - Used to fill or replace missing values with a meaningful value, such as "unknown".
#
# dropna with subset - Used to drop rows that have missing values in a specific column.
#
# Statistical functions: min, max, mean, median, mode, sum - Used to get summary statistics from numerical columns.
#
# agg / aggregate - Used to apply multiple aggregation functions at once on a column, such as sum, mean, min, and max together.
#
# sort_values - Used to sort data in ascending or descending order, either numerically or alphabetically, based on one or more columns.
#
# idxmax - Used to return the index position of the maximum value in a column, rather than the maximum value itself.

#convert purchase date to datetime
pur["purch_date"]=pd.to_datetime(pur["purch_date"])
print(pur["purch_date"].dtype)
# convert paid to numeric

print(pur["purch_date"].dt.month)
print(pur["purch_date"].dt.day)
print(pur["purch_date"].dt.year)


prod["cost"]=(prod["cost"].str.replace(r"[\$]","",regex=True).astype(float))
print(prod["cost"].sum())
pur["paid"] = pur["paid"].str.replace(r"[$,]", "", regex=True).astype(float)
print(pur["paid"].sum())
# back slash ensure only pick the dollar sign




# missing values   -------> data preprocessing   and functions are used isna() ,dropna(),fillna()


# find the missing customer information
missing_customers=cust.isna().sum()
print(missing_customers)

# replace missing  emails
cust["email"]=cust["email"].fillna("unknows email ")
cust["email"].value_counts().head()
print(cust["email"].value_counts())

# remove customers without an email

email_cust=cust.dropna(subset=["email"])
print('original customers:',len(cust))
print('customer with email : ',len(email_cust))

# statistical operations :
# mean() median(0 , mode(),max(),min(0,sum(0,count()

# understand product price range --> cheapest ,most expensive ,average

print("cheapest :",prod["cost"].min())
print('most expensive',prod["cost"].max())
print('average',round(prod["cost"].mean(),2))

# aggregations : ----> agg() or aggregate ()

# summary of the paid column
# pur["paid"] = pd.to_numeric(pur["paid"])
# payment_summary = pur["paid"].agg(["sum", "mean", "max", "min"])

# print(payment_summary)


# sorting values :
# create an alphbetical customer directory
customer_directory=(cust[["id","first_name","last_name","city","state"]].sort_values(by=[ "first_name","last_name" ]).head(10))
print(customer_directory)


#idmax(0 --returns the index of the first occurence of the maximum value
#
# index_max_paid=pur["paid"].idmax()
# print(index_max_paid)


# group by : ---> it works on three stages
 # split ()---> split into groups
 # apply ()--->  10+20+30/3 b--> 50+40/2
 # combine ()


# product portfolio by company

company_summary=(prod.groupby("company",dropna=False).
                 agg(avg_cost=("cost","mean"),prod=("id","count")  ))
print(company_summary)

# top 5 dates having the highest sales
daily_sales = pur.groupby("purch_date")["paid"].sum().sort_values(ascending=False)
print(daily_sales)

# altering index : ---> reset _index   change the index opposite to the set_index


cutomers_by_id =cust.set_index("id")
print(cutomers_by_id.loc[100])
cutomers_by_id.reset_index(inplace=True) # reset the index again to default values
cutomers_by_id.head(10)

# pivot table : ------>

# pd.pivot_table(df,index,columns,value,aggfunc)

sales=pur.merge(prod,left_on="product_num",right_on="id",suffixes=("_purchaes","_product"))
print(sales)
sales=sales.merge(cust[["id","gender","state"]],left_on="customer_num",right_on="id")
pd.set_option("display.max_columns", None)
print(sales)


# payment by gender and company
pivot_gender_company=pd.pivot_table(sales,index="gender",columns="company",values="paid",aggfunc=sum,fill_value=0)
print(pivot_gender_company)

# customer count by state and gender
customer_count=pd.pivot_table(cust,index="state",columns="gender",values="id",aggfunc="count",fill_value=0)
customer_count["total"]=customer_count.sum(axis=1)
print(customer_count.sort_values(by="total",ascending=False))


# cross tab : used for frequency or count analysis of categorical data

# how many sttate wise gender count

gender_state=pd.crosstab(cust["state"],cust["gender"])
print(gender_state.loc[["California","Texas","New York"]])


# melt () converting a dataframe from wide format to long format

# convert state -gender report to analytical format
wide=pd.crosstab(cust["state"],cust["gender"]).reset_index()
print(wide)
print(wide.melt(id_vars="state",var_name="gender",value_name="customers"))
# var --> column name , count column name is customer s

# exporting data

# export product price report to excel

product_price_report=(prod[["id","product","company","cost"]].sort_values("cost",ascending=False))
print(product_price_report)
product_price_report.to_excel("product_price_report.xlsx",index=False)