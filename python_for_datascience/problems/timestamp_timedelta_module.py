from datetime import datetime, timedelta
# Don't make any changes to the above code

# Write your code here
def analyze_timestamps(n, timestamps):
    day_of_week=[]
    for day in timestamps:
            day=day.strftime('%A')
            day_of_week.append(day)


