import datetime

week_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
now = datetime.datetime.now()
day = datetime.datetime.weekday(now)

first_day = datetime.date(2021, 5, 1)
last_day = datetime.date(2021, 5, 31)
print(day + 1)

exact_first_day = datetime.datetime.weekday(first_day)
exact_last_day = datetime.datetime.weekday(last_day)

print(week_days[exact_first_day])
print(week_days[exact_last_day])