import datetime
import time

print(datetime.datetime.now())
print(datetime.datetime(2015, 2, 27, 11, 10, 49, 55, 53))
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)
print(datetime.datetime.fromtimestamp(time.time()))
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
str(delta)

# Sleep until date
halloween2017 = datetime.datetime(2017, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2017:
    time.sleep(1)

# Convert to strings
oct21st = datetime.datetime(2017, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
oct21st.strftime('%I:%M %p')
oct21st.strftime("%B of '%y")

# Convert from strings
datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
datetime.datetime.strptime("October of '15", "%B of '%y")
datetime.datetime.strptime("November of '63", "%B of '%y")