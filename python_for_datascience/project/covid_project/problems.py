import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# STEP 1: READ EXCEL FILES


confirmed = pd.read_excel('confirmed.xlsx')
deaths = pd.read_excel('deaths.xlsx')
recovered = pd.read_excel('recovered.xlsx', header=1)

# Store all datasets in a dictionary
datasets = {'Confirmed': confirmed,'Deaths': deaths,'Recovered': recovered}


# STEP 2: CHECK DATA STRUCTURE

for name, df in datasets.items():
    print(f"\n{name} dataset")
    print("Shape:", df.shape)
    print("Data types:")
    print(df.dtypes)
    print("Missing values:")
    print(df.isnull().sum()[df.isnull().sum() > 0])


# STEP 3: CONVERT DATE COLUMN NAMES


for name, df in datasets.items():

    location_columns = list(df.columns[:4])

    date_columns = pd.to_datetime(df.columns[4:],format='%m/%d/%y' )

    df.columns = location_columns + list(date_columns)




# STEP 4: HANDLE MISSING PROVINCE NAMES
for name, df in datasets.items():
    df['Province/State'] = (df['Province/State'].fillna('All Provinces')    )


# STEP 5: PROBLEM 1
# PEAK DAILY NEW CASES IN GERMANY, FRANCE, ITALY


country = ['Germany', 'France', 'Italy']
country_cases = confirmed[confirmed['Country/Region'].isin(country)].copy()
data = country_cases.columns[4:]
daily_cases = country_cases.copy()
daily_cases[data] = country_cases[data].diff(axis=1)
highest_single_day_surge = ( daily_cases.groupby('Country/Region')[data].sum())
peak_date = highest_single_day_surge.idxmax(axis=1)
peak_cases = highest_single_day_surge.max(axis=1)
peak_sum = pd.DataFrame({'peak_date': peak_date,'peak_cases': peak_cases}).sort_values(by='peak_cases', ascending=False)
peak_sum['peak_date'] = pd.to_datetime(peak_sum['peak_date']).dt.strftime('%d-%m-%Y')

print(" Peak Daily New Cases")
print(peak_sum)

# Plot the results
peak_sum['peak_cases'].plot(kind='bar',figsize=(9, 5))

plt.title('Peak Daily New COVID-19 Cases by Country')
plt.xlabel('Country')
plt.ylabel('Maximum Daily New Cases')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# STEP 6: PROBLEM 2
# RECOVERY RATE: CANADA VS AUSTRALIA



target_date = pd.to_datetime('2020-12-31')

countries = ['Canada', 'Australia']

results = []
for country_name in countries:
        confirmed_country = confirmed[confirmed['Country/Region'] == country_name]
        recovered_country = recovered[recovered['Country/Region'] == country_name]
        confirmed_total = confirmed_country[target_date].sum()
        recovered_total = recovered_country[target_date].sum()


        recovery_rate = (recovered_total / confirmed_total * 100 if confirmed_total > 0 else np.nan)

        results.append({'Country': country_name,'Confirmed Cases': confirmed_total,        'Recovered Cases': recovered_total,
            'Recovery Rate (%)': recovery_rate })


recovery_summary = pd.DataFrame(results)
recovery_summary = recovery_summary.sort_values(by='Recovery Rate (%)',ascending=False)

print(" Recovery Rate Comparison")
print(recovery_summary.to_string(index=False))
best_country = recovery_summary.iloc[0]['Country']

print(f"\nAccording to the recovery-rate metric, " f"{best_country} had the higher recovery rate.")


# calculate and compare the death rates across canadian provinces

canada_conf=confirmed[confirmed['Country/Region']=='Canada'].copy().set_index('Province/State')
canada_deaths=deaths[deaths['Country/Region']=='Canada'].copy().set_index('Province/State')
latest_date=canada_conf.columns[-1]
confir_latest=canada_conf[latest_date]
deaths_latest=canada_deaths[latest_date]


death_rate = ( deaths_latest.div(confir_latest.where(confir_latest != 0)) * 100)

res=pd.DataFrame({
    'Confirmed Cases': confir_latest,'Deaths':deaths_latest,'death_rate': death_rate})
print(res)


import matplotlib.pyplot as plt
import seaborn as sns

# Sort provinces by death rate
res_sorted = res.sort_values(by='death_rate', ascending=True)

plt.figure(figsize=(12, 7))

sns.barplot(  data=res_sorted.reset_index(),  x='death_rate',   y='Province/State')

plt.title('COVID-19 Death Rate by Province in Canada')
plt.xlabel('Death Rate (%)')
plt.ylabel('Province / State')

plt.tight_layout()
plt.show()










# Province with the highest death rate
highest_province = res['death_rate'].idxmax()
highest_rate = res['death_rate'].max()

print(f"Highest death rate: {highest_province}")
print(f"Death rate: {highest_rate:.2f}%")



# TRANSFROM THE DATA

latest=confirmed[latest_date].to_frame(name='confirmed').reset_index(drop=True).join(
    recovered[latest_date].to_frame(name='recovered').join(
        deaths[latest_date].to_frame(name='deaths')
    )
)
latest.insert(0,'Date',latest_date)
print(latest)


# Make a copy so the original DataFrame remains unchanged
deaths_copy = deaths.copy()

# Convert column labels to strings
deaths_copy.columns = [
    str(col) if isinstance(col, pd.Timestamp) else col
    for col in deaths_copy.columns
]

# Transform wide format to long format
death_in_long = deaths_copy.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],var_name='Date',
    value_name='Deaths')
death_in_long['Date'] = pd.to_datetime(death_in_long['Date'],format='%Y-%m-%d %H:%M:%S')

print(death_in_long)
# TOP 5 COUNTRIES WITH HIGHEST AVERAGE DAILY DEATHS

ttl_deaths = ( death_in_long[death_in_long['Date'] == latest_date]
    .groupby('Country/Region')['Deaths']
    .sum()
    .sort_values(ascending=False))

top_5 = ttl_deaths.head(5).reset_index(name='Deaths')

# Convert deaths into lakhs for a more readable chart
top_5['Deaths_Lakhs'] = top_5['Deaths'] / 100000

plt.figure(figsize=(10, 6))

sns.barplot(
    data=top_5,
    x='Country/Region',
    y='Deaths_Lakhs'
)

plt.title('Top 5 Countries with Highest Reported COVID-19 Deaths')
plt.ylabel('Total Deaths (in Lakhs)')
plt.xlabel('Countries')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# total deaths evolved over time in the united states

us_deaths=death_in_long[death_in_long['Country/Region']=='US']
us_deaths_over_time=(us_deaths.groupby('Date')['Deaths'].sum().reset_index())

us_deaths_over_time['Deaths_Lakh']=(us_deaths_over_time['Deaths']/1000000)

#creating a line chart
plt.figure(figsize=(10, 6))
sns.lineplot(
    data=us_deaths_over_time,
    x='Date',
    y='Deaths_Lakh'
)
plt.title('Evolution of Cumulative COVID-19 Deaths in the United States')
plt.xlabel('Date')
plt.ylabel('Total Deaths (in Lakhs)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# death cases in unites states evolved over time

# DATA MERGING
long_datasets = {}

id_cols = ['Province/State', 'Country/Region', 'Lat', 'Long']

for name, df in datasets.items():

    date_cols = df.columns[4:]

    df_long = (
        df.set_index(id_cols)[list(date_cols)]
        .stack()
        .reset_index()
    )

    df_long.columns = id_cols + ['Date', name]

    long_datasets[name] = df_long

covid_data = pd.merge(
    long_datasets['Confirmed'],
    long_datasets['Deaths'][['Country/Region', 'Date', 'Deaths']],
    on=['Country/Region', 'Date'],
    how='inner'
)
covid_data = pd.merge(
    covid_data,
    long_datasets['Recovered'][['Country/Region', 'Date', 'Recovered']],
    on=['Country/Region', 'Date'],
    how='inner'
)

 # MONTH SUM FOR DEATHS, RECOVERED, CONFIRMED
covid_data['Month'] = covid_data['Date'].dt.to_period('M')
monthly_data = covid_data.groupby(['Country/Region', 'Month'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
print(monthly_data)


# MONTHLY DATA FOR THE UNITED STATES, ITALY, BRAZIL

countries = ['US', 'Italy', 'Brazil']

filtered_data = monthly_data[monthly_data['Country/Region'].isin(countries)].copy()

print(filtered_data.head())
# CREATE A PLOT
import matplotlib.pyplot as plt

for country in countries:

    country_data = filtered_data[
        filtered_data['Country/Region'] == country
    ].sort_values('Month')

    plt.figure(figsize=(12, 6))

    plt.plot(country_data['Month'].astype(str),
             country_data['Confirmed'],
             label='Confirmed Cases', marker='o')

    plt.plot(country_data['Month'].astype(str),
             country_data['Deaths'],
             label='Deaths', marker='o')

    plt.plot(country_data['Month'].astype(str),
             country_data['Recovered'],
             label='Recoveries', marker='o')

    plt.title(f'Monthly COVID-19 Trends: {country}')
    plt.xlabel('Month')
    plt.ylabel('Sum of Daily Cumulative Totals')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# THREE COUNTRIES WITH HIGHEST AVERAGE DEASH RATE


data_2020 = covid_data[ covid_data['Date'].dt.year == 2020].copy()

#
data_2020['Death_Rate'] = (data_2020['Deaths'] / data_2020['Confirmed'].replace(0, np.nan)) * 100


avg_death_rate = (
    data_2020.groupby('Country/Region')['Death_Rate']
    .mean()
    .dropna()
    .sort_values(ascending=False)
    .head(3)
)

print(avg_death_rate)

# COMPARE TOTAL RECOVERIES AND DEATHS IN SOUTH AFRICA
south_africa = covid_data[ covid_data['Country/Region'] == 'South Africa'].copy()
sa_daily = south_africa.groupby('Date')[ ['Confirmed', 'Deaths', 'Recovered']].sum()
latest = sa_daily.sort_index().iloc[-1]
print("Total Confirmed Cases:", latest['Confirmed'])
print("Total Deaths:", latest['Deaths'])
print("Total Recoveries:", latest['Recovered'])

if latest['Deaths'] != 0:
    ratio = latest['Recovered'] / latest['Deaths']
    print("Recovery-to-Death Ratio:", round(ratio, 2))
else:
    print("Recovery-to-Death Ratio: Undefined because deaths are zero.")

# Filter US data for the required period
us_data = covid_data[
    (covid_data['Country/Region'] == 'US') &
    (covid_data['Date'] >= '2020-03-01') &
    (covid_data['Date'] <= '2021-05-31')
].copy()

us_daily = us_data.groupby('Date')[
    ['Confirmed', 'Deaths', 'Recovered']
].sum()
us_monthly = us_daily.resample('ME').last()

us_monthly['Recovery_Ratio'] = (
    us_monthly['Recovered'] /
    us_monthly['Confirmed'].replace(0, np.nan)
) * 100

print(us_monthly[['Confirmed', 'Recovered', 'Recovery_Ratio']])


highest_month = us_monthly['Recovery_Ratio'].idxmax()

print("\nMonth with highest recovery ratio:", highest_month.strftime('%B %Y'))
print("Highest recovery ratio:", round( us_monthly.loc[highest_month, 'Recovery_Ratio'], 2), "%")