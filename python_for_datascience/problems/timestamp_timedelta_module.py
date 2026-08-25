from datetime import datetime, timedelta


# Don't make any changes to the above code

# Write your code here
def analyze_timestamps(n, timestamps):
    dt_objs = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in timestamps]

    earliest = min(dt_objs).strftime('%Y-%m-%d %H:%M:%S')
    latest = max(dt_objs).strftime('%Y-%m-%d %H:%M:%S')
    days = []
    for dt in dt_objs:
        days.append(dt.strftime('%A'))
    print(f'Days of the week: {days}')

    print(f'Earliest Timestamp: {earliest}')
    print(f'Latest Timestamp: {latest}')

    rs = []
    for day in timestamps:

        if datetime.strftime(datetime.strptime(day, '%Y-%m-%d %H:%M:%S'), "%A") == 'Friday':
            re = datetime.strftime(datetime.strptime(day, '%Y-%m-%d %H:%M:%S') + timedelta(days=3), '%Y-%m-%d %H:%M:%S')
            rs.append(re)
        else:
            re = datetime.strftime(datetime.strptime(day, '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
            rs.append(re)
    print(f'Rescheduled Timestamps: {rs}')


