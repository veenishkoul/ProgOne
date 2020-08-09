#This script checks for the leap year
# This is part of the python learning

def is_leap(is_leap_year):
    leap = False
    if is_leap_year % 4 == 0:
        if is_leap_year % 100 == 0:
            if is_leap_year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap


print("Enter the year:")
raw_year = input()
is_leap_year = int(raw_year)
print(is_leap(is_leap_year))
