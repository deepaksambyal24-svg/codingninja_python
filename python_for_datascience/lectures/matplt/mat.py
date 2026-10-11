import mtplot.pyplot as plt
import numpy as np
import pandas as pd
import _p as sns
airline=pd.read_csv("airline.csv")
print(airline.head())
airline["flight_date"]=pd.to_datetime(airline['flight_date'])
airline["month"]=airline["flight_date"].dt.month
print(airline.head())
monthly_passenders=(airline.groupby("month")["passengers"].sum())
plt.figure(figsize=(10,5))
plt.plot(monthly_passenders.index,monthly_passenders.values,marker='o',color='blue',linestyle='-',linewidth=2)
plt.title('monthly passenger trend')
plt.xlabel('month')
plt.ylabel('passengers')
plt.grid(True)
plt.show()


## identify top 5 routes generating the most revenue

route_revenue=(airline.groupby("route")["total_revenue_inr"].sum().sort_values(ascending=False).head())

plt.bar(route_revenue.index,route_revenue.values)

plt.title("top 5 routes by revenue")

plt.xlabel("route")

plt.ylabel("total revenue")

plt.xticks(rotation=45)

plt.yticks(rotation=45)

plt.show()

## no of flights for each airline

flight_count=airline["airline"].value_counts()

flight_count




flight_count.plot(kind="bar")

plt.title("number of flights per airline")

plt.xlabel("airline")

plt.ylabel("no of flights")

plt.show()

# delay distribution in 30 mins range

# create a bin
bins=np.arange(0,181,30)
plt.hist(airline["delay_minutes"],bins=bins,edgecolor='black',linewidth=2)
plt.title('distibutinof foight delay ')
plt.xlabel('delay minutes')
plt.ylabel('number of flights')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()



# BOX PLOT : --- > DETECT UNUSUAL FLIGHT DELAYS USING BOXPLOT

plt.figure(figsize=(6,5))
plt.boxplot(airline["delay_minutes"])
plt.title('boxplot delays  ')
plt.xlabel('delay minutes')
plt.ylabel('number of flights')
plt.grid(True)

plt.show()

# HEAT MAP CHART USING SEABORN AND CORELAATION

# numeric_data=airline[["passengers","avg_fare_inr","ticket_revenue_inr","delay_minutes","customer_rating"]]
# corr=numeric_data.corr()
# sns.heatmap(corr,annot=True)
# plt.title('heatmap correlation')
# plt.show()


## compare fare distributions between airlines using kde plot (kernel density estimation )

# kde-gives a smooth curve showing where are concentrated

sns.kdeplot(data=airline, x="avg_fare_inr", hue="airline", fill=True)
plt.title('average fare distibutin by airline')
plt.xlabel('average fare (inr)')
plt.show()

# compare revenue distribution across booking channel

plt.figure(figsize=(10,6))
sns.violinplot(data=airline, x="booking_channel",y='total_revenue_inr', hue="airline")
plt.title('total revenue by airline')
plt.xlabel('booking channel')
plt.ylabel(' revenue')
plt.show()


# what percentage of flights were complted and cancelled

flight_status=airline["flight_status"].value_counts()
plt.pie(flight_status,labels=flight_status.index,autopct='%1.1f%%')
plt.title('flight status by airline percent')
plt.show()




# find fare and delay have any relation or not

plt.figure(figsize=(10,6))
plt.scatter(airline["avg_fare_inr"],airline["delay_minutes"])
plt.title('average fare delay by airline')
plt.xlabel('average fare (inr)')
plt.ylabel('number of flights')
plt.show()