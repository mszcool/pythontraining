#
# Working with time deltas
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# basic time delta
simple = timedelta(days=365, hours=5, minutes=1, seconds=35)
print(simple)

# So take today
now = datetime.now()
print("Today is: ", now)

# One year from now
nowPlusOneYear = now + timedelta(days=365)
print("In one year is ", nowPlusOneYear)

# More complex time detal
nowPlusOneYearAndFiveHours = now + simple
print("IN one year, 5 hours, 1 minute and 35 seconds it is: ", nowPlusOneYearAndFiveHours)

# Calculate back in time
t = datetime.now() - timedelta(weeks = 1)
s = t.strftime("%A %B %Y %d")
print(s)

# Calculate how many days to the next April 1st
today = date.today()
aprilFirst = date(today.year + 1, 4, 1)
# aprilFirst = date(today.year, 4, 1)
if(aprilFirst > today):
    print("Until next April fools day is ", (aprilFirst - today).days)
elif(aprilFirst < today):
    print("April Fool's day went by %d days ago" % (today - aprilFirst).days)

# Calculate days until my birthday
today = date.today()
bday = date(today.year, 7, 15)
diff = (bday - today).days
if diff > 0:
    print("Your bday is in %d days" % diff)
elif diff < 0:
    print("Your bday was %d days ago" % (diff*-1))
else:
    print("Happy birthday!")

# Don't do this: tomorrow = date(today.year, today.month, today.day + 1)
tomorrow = today + timedelta(days=1)
print(tomorrow)
