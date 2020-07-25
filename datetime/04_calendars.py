#
# Working with different types of calendars
#

import calendar
from datetime import datetime

# Keep now if we need it
now = datetime.now()

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(now.year, now.month, 0, 0)
print(st)
st = c.formatmonth(now.year, now.month, 10, 2)
print(st)

# create an HTML formatted calendar
c = calendar.HTMLCalendar(calendar.MONDAY)
ht = c.formatmonth(now.year, now.month,False)
print(ht)

#
# loop over days in a month
# zeores mean that the day of the week is in an overlapping month
c = calendar.TextCalendar(calendar.MONDAY)
for i in c.itermonthdates(now.year, now.month):
    print(i)

# Utilities for given locale such as names of days and months in full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

for day in calendar.day_abbr:
    print(day)

# Calculate days based on a rule:
#
print("Meetings happening every 1st friday in a month:")
# Note: it runs from 1 until < 13 with the range() below
for m in range(1, 13):
    cal = calendar.monthcalendar(now.year + 1, m)
    weekone=cal[0]
    weektwo=cal[2]
    if(weekone[calendar.FRIDAY] != 0):
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    
    #meetdate=datetime(now.year + 1, m, meetday)
    #print(meetdate.strftime("%A, %Y/%m/%d"))

    print("%10s, %02d" % (calendar.month_name[m], meetday))
