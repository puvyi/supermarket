import Supermarket
import pandas as pd

def get_data():
    customer_per_minute = pd.read_csv('customer_per_minute.csv', index_col=0)
    customer_per_minute = customer_per_minute.astype(int)
    data =[]
    for value in customer_per_minute['customer_no_count']:
        data.append(value)
    return data
