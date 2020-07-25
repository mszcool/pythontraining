#
# Working with date/time libraries
#

from datetime import date
from datetime import time
from datetime import datetime

def main():

    # Get today's date
    today = date.today()
    print("Today's date is ", today)

    # Print the components of a date
    print("Date components: ", today.day, today.month, today.year)

    # Get the weekday of today
    print("Today's weekday number ", today.weekday())
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    print("Today's weekday is ", days[today.weekday()])

    # Get today's date and time
    todayNow = datetime.now()
    print("Now is ", todayNow)

    # Get the time 
    nowTime = datetime.time(todayNow)
    nowDay = datetime.now().day
    print("Now time", nowTime, "Now day", nowDay)

if __name__ == "__main__":
    main()