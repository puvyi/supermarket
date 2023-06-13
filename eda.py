import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Dataframes for each day data
monday = pd.read_csv('data/monday.csv', sep=';', parse_dates=['timestamp'])
tuesday = pd.read_csv('data/tuesday.csv', sep=';', parse_dates=['timestamp'])
wednesday = pd.read_csv('data/wednesday.csv', sep=';', parse_dates=['timestamp'])
thursday = pd.read_csv('data/thursday.csv', sep = ';', parse_dates=['timestamp'])
friday = pd.read_csv('data/friday.csv', sep=';', parse_dates=['timestamp'])

# List of all days data
days_data = [monday,tuesday, wednesday, thursday, friday]

# Creating a day feature for each day dataframe
monday['day'] = 'monday'
tuesday['day'] = 'tuesday'
wednesday['day'] = 'wednesday'
thursday['day'] = 'thursday'
friday['day'] = 'friday'

# Setting timestamp as the index for all the day dataframes
for day in days_data:
    #day.timestamp = pd.to_datetime(day.timestamp)
    day.set_index('timestamp', inplace=True)

# Getting all customers who need to be checked out
def get_non_checkout(df):
    non_checkout_customers = df['customer_no'].max()
    checkout_customers = []
    for c_id in range(non_checkout_customers):
        if not 'checkout' in df[df['customer_no'] == c_id+1]['location'].values:
            checkout_customers.append(c_id+1)
    return checkout_customers

# Make a LIST of customers to be checked out
customers_to_checkout = []
for day in days_data:
    customers_to_checkout.append(get_non_checkout(day))

# Adds a extra line to the dataframe
def add_checkout(df, customer_nos, date, day):
    df_fill = pd.DataFrame()
    for p_id in customer_nos:
        df_tmp = pd.DataFrame(data=[[p_id, 'checkout', day]], index=[pd.to_datetime(f'2019-09-{date} 21:59:00')], columns=['customer_no', 'location', 'day'])
        df = pd.concat([df, df_tmp])
    return df


filled_data = []
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
date = ['02', '03', '04', '05', '06']
for i, day in enumerate(days_data):
    filled_data.append(add_checkout(day, customers_to_checkout[i], date[i], weekdays[i]))


total = pd.concat(filled_data)

### Setting up time step to 1 min
df = total.groupby(['customer_no', 'day']).resample('1Min').ffill()

df['from'] = df['location'].shift(1)

# None values refilled with checkout
df.fillna('checkout', inplace=True)

# Normalizing the dataframe df
tm = pd.crosstab(df['from'], df['location'], normalize='index')

