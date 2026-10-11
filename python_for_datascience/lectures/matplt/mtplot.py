import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


airline = pd.read_csv('airline.csv')


print(airline.head())
print(airline.head())
print(airline.head().T)


# no of  flights for each airline
flight_count=airline['airline'].value_counts()
print(flight_count)

flight_count.plot(kind='bar')
plt.title('airline flight count')

plt.xticks(rotation=90)
plt.xlabel('Airline')
plt.ylabel('Flight Count')
plt.show()


# idenfity top 5 route generating he most revenue

route_revenue=(airline.groupby("route")['total_revenue_inr'].sum().sort_values(ascending=False).head())
print(route_revenue)
plt.bar(route_revenue.index,route_revenue.values)
plt.title('route revenue')
plt.xlabel('Route')
plt.ylabel('Flight Count')
plt.xticks(rotation=10)         # rotate the y lables into 10 degree
plt.yticks(rotation=20)
plt.show()


# # passenger trend thoughout the year
# passenger trend throughout the year

airline["flight_date"] = pd.to_datetime(airline["flight_date"])
airline["month"] = airline["flight_date"].dt.month

monthly_passenger=(airline.groupby("month")["passengers"].sum() )

print(monthly_passenger)
plt.plot(monthly_passenger.index,monthly_passenger.values,marker='o',linestyle='--',linewidth=2)
plt.title('monthly_passenger')
plt.xlabel('Month')
plt.figure(figsize=(10,5))
plt.bar(monthly_passenger.index,monthly_passenger.values)
plt.ylabel('passengers')
plt.grid(True)
plt.show()




# use numpy for charts

# create a bin for creating a histrogram
# DELAY DISTRIBUTION IN 30 mins range
bins =np.arange(0,181,30)
plt.hist(airline["delay_minutes"],bins=bins,edgecolor='black',linewidth=2,color='blue')
plt.title('distribution of delay_minutes')
plt.xlabel('delay_minutes')
plt.ylabel('passengers')
plt.grid(True)
plt.show()


# detect unusual flight delays using box plot

plt.figure(figsize=(10,5))
plt.boxplot(airline["delay_minutes"])
plt.title('flight_plot_ boxplot')
plt.ylabel('delay_minutes')

plt.grid(True)
plt.show()


# SEABORN

numeric_data=airline[["passengers","avg_fare_inr","ticket_revenue_inr"
    ,"delay_minutes","customer_rating"]]
corr=numeric_data.corr()
sns.heatmap(corr,annot=True)
plt.title("airline correlation heatmap matrix ")
plt.show()


# compare fare distributions between arilines using kde plot ( kernel density estimation )

# kde gives a smooth curve showing where values are concentrated
# it is module of seaborn

sns.kdeplot(data=airline,x="avg_fare_inr",hue="airline",fill=True)
plt.title("average fare distribution by airline ")
plt.xlabel("average fare (INR)")
plt.show()


# compare revenue distributin across boooking channel

plt.figure(figsize=(10,6))
sns.violinplot(data=airline,x="booking_channel",y="total_revenue_inr")
plt.title("revenue violin plot")

plt.xlabel("booking channel")
plt.ylabel('no of flights')

plt.show()


# PI CHART ----> WHAT PERCENTAGE OF FLIGHTS WERE COMPLETED AND CACNCELLED
flight_status=airline["flight_status"].value_counts()
plt.pie(flight_status,labels=flight_status.index,autopct="%1.1f%%")
plt.title('flight status')
plt.show()


# find fare and delay are related
plt.figure(figsize=(10,6))
plt.scatter(airline["avg_fare_inr"],airline["delay_minutes"])
plt.title('delay_minutes scatter')
plt.xlabel('avg fare ')
plt.ylabel("delay")
plt.show()
#


# seaborn scatterplt

sns.scatterplot(data=airline,x='avg_fare_inr',y='delay_minutes',hue='airline')
plt.show()