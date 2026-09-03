import random
from datetime import datetime,timedelta

def random_dates(start_date, end_date):
    end_day = int(end_date[-2::])
    start_day = int(start_date[-2::])
    random_days = start_day + random.randint(0, end_day - start_day + 1)
    random_day_str = str(random_days).zfill(2)
    year, month, _ = start_date.split('-')

    year = start_date[:4]
    month = start_date[5:7].zfill(2)

    result = f'{year}-{month}-{random_day_str}'
    return result

date.str