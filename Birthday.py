from datetime import date

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31


def calculate_exact_age(birthday, birthmonth, birthyear):
    today = date.today()

    year = today.year - birthyear
    month = today.month - birthmonth
    day = today.day - birthday

    if day < 0:
        month = month - 1

        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year

        day = day + days_in_month(prev_month, prev_year)

    # Fix negative months
    if month < 0:
        year = year - 1
        month = month + 12

    return year, month, day


birth_day = int(input("Enter the birth day: "))
birth_month = int(input("Enter the birth month: "))
birth_year = int(input("Enter the birth year: "))

try:
    birth_date = date(birth_year, birth_month, birth_day)
except ValueError:
    print("Invalid date entered!")
    exit()

if birth_date > date.today():
    print("Birth date cannot be in the future!")
    exit()

years, months, days = calculate_exact_age(birth_day, birth_month, birth_year)

print("Exact Age:")
print(years, "years,", months, "months,", days, "days")
