import pandas as pd
import matplotlib.pyplot as plt
# covid-19 data analysis case study

confirmed=pd.read_excel('confirmed.xlsx')
deaths=pd.read_excel('deaths.xlsx')
recovered=pd.read_excel('recovered.xlsx',header=1)
print(confirmed.T)
print(deaths.T)
print(recovered.T)  # there is an extra column on heading

print(confirmed.isna().sum())

# find the top countries and plot confirmed cases
latest_date=confirmed.columns[-1]
country_total=confirmed.groupby("Country/Region")[latest_date].sum()
top_3=country_total.nlargest(3)
print(top_3)


for c in top_3.index:
    country_data = confirmed[confirmed['Country/Region'] == c]
    cases = country_data.iloc[:, 4:].sum()

    cases.index = pd.to_datetime(cases.index, format='%m/%d/%y')

    plt.plot(cases.index, cases.values, label=c)

plt.legend()
plt.title('Confirmed cases over time')
plt.xlabel('Date')
plt.ylabel('Confirmed cases')
plt.xticks(rotation=90)
plt.show()


# plot china by province

china=confirmed[confirmed["Country/Region"]=="China"]

china.set_index("Province/State").iloc[:,3:].T.plot()

plt.title("covid 19 cases in china province")

plt.xlabel("Date")

plt.ylabel("confirmed cases")

plt.show()

print(confirmed.isnull().sum())
print(recovered.isnull().sum())
print(deaths.isnull().sum())

confirmed['Province/State']=(confirmed["Province/State"].fillna('all province'))
deaths['Province/State']=(confirmed["Province/State"].fillna('all province'))
recovered['Province/State']=(confirmed["Province/State"].fillna('all province'))
print(confirmed.isnull().sum())
print(deaths.isnull().sum())
print(recovered.isnull().sum())