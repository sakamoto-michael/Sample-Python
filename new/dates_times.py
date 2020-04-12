# Working with dates and times in Python
import datetime
import pytz # Used for timezones

# Working with dates (no time)
new_date = datetime.date(2020, 4, 12)
today = datetime.date.today()
# In 'today' can access .year, .month, and .daysett

# Check the day of the week given a date
today.weekday() # Returns Monday 0 - Sunday 6
today.isoweekday() # Returns Monday 1 - Sunday 7

# Time delta - can add or subtract time deltas to/from a date
time_delta = datetime.timedelta(days=7)
one_week_from_today = today + time_delta

# Calculating time difference between two dates
bday = datetime.date(2020,11,14)
till_bday = bday - today
# print(till_bday.total_seconds())

# Hours, minutes, seconds, microseconds (no date)
time = datetime.time(10, 45, 30, 100000)

# Date and time
full_time = datetime.datetime(2020, 4, 12, 10, 45, 30, 100000)
# print(full_time)
# print(full_time.date())
# print(full_time.time())
# print(full_time + time_delta)

# Getting the current time
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

# Explicitly setting UTC (timezone aware)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)  

# Converting from UTC to another time zone
dt_jst = dt_utcnow.astimezone(pytz.timezone('Asia/Tokyo'))
print(dt_jst)

# (Getting a list of pytz timezones)
# for tz in pytz.all_timezones:
#   print(tz)

# Making a naive datetime timezone aware
dt_jst = datetime.datetime.now()
jst_tz = pytz.timezone('Asia/Tokyo')
dt_jst = jst_tz.localize(dt_jst)
# Now it can be converted to Eastern Time
dt_east = dt_jst.astimezone(pytz.timezone('US/Eastern'))
print(f'The current Eastern time is: {dt_east}')

# Formatting a datetime based on format code
# Guide here: https://docs.python.org/3.5/library/datetime.html
dt_east_formatted = dt_east.strftime('%A, %B %d %Y - %I:%M %p')
print(f'The current Eastern time (formatted) is: {dt_east_formatted}')

# Converting a string to a datetime
dt_str = 'April 12, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# Conclusion:
# strftime - Datetime to String
# strptime - String to Datetime