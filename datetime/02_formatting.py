#
# Formatting of date and time
#

from datetime import datetime

def main():

    # String Control Codes used for formatting
    now = datetime.now()
    print(now.strftime("Current year is: %Y or %y"))

    # Custom Formatting for dates
    # %y/%Y - Year, %a/%A - weekday, %b/%B/%m - month, %d - day of month
    print(now.strftime("%a, %d / %b / %y"))
    print(now.strftime("%A, %d / %B / %Y"))
    print(now.strftime("%A, %d / %m / %Y"))
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

    # Custom formatting for time
    # %I/%H - 12/24 Hour, %M - minute, %S - seconds, %p locale's AM/PM
    print(now.strftime("Current time: %H:%M:%S"))
    print(now.strftime("Current time: %I:%M:%S %p"))

    print(now.strftime("%d-%b-%Y %H:%M:%S"))

if __name__ == "__main__":
    main()