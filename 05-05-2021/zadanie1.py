import datetime

now = datetime.datetime.now();
weekAgo = datetime.datetime(2021,4,28);
monthLater = datetime.datetime(2021,6,5) + datetime.timedelta(hours = 12)

print(now)
print(weekAgo)
print(monthLater)