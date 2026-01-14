#Gregorian Calendar only
def check_leap(yr):
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
        return True
    else:
        return False

def check_valid_day(dy):
    if 31 >= dy > 0:
        return True
    else:
        return False

def check_valid_day_in_month(mth, dy, yr):
    if mth in [4, 6, 9, 11]:  # April, June, September, November have 30 days
        if 0 < dy <= 30:
            return True
        else:
            return False
    elif mth == 2 and check_leap(yr) == True:  # February in leap year
        if 0 < dy <= 29:
            return True
        else:
            return False
    elif mth == 2 and check_leap(yr) == False:  # February in non-leap year
        if 0 < dy <= 28:
            return True
        else:
            return False
    elif mth in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
        if 0 < dy <= 31:
            return True
        else:
            return False
    else:
        return False

year = int(input("What is the year?(yyyy): "))
day = int(input("What is the day of the month? (1-31): "))

if not check_valid_day(day):
    print("The entered date is not valid")
    exit()

month = int(input("What is the month number? (1-12): "))

if not check_valid_day_in_month(month, day, year):
    print("The entered date is not valid")
    exit()

if month < 3:
    month += 12
    year -= 1

C = year // 100
D = year % 100

F = (day + (13 * (month + 1)) // 5 + D + D // 4 + C // 4 - 2 * C) % 7

wd = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# noinspection PyTypeHints
print("The day of the week is " + wd[int(F)])
