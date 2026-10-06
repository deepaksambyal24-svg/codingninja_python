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

