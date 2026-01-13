from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__)

# ---------- Leap year logic ----------

def is_leap_year(year):
    # Gregorian leap-year rule
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# ---------- Days-in-month and validation ----------

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

def check_valid_day(dy):
    return 0 < dy <= 31

def check_valid_day_in_month(mth, dy, yr):
    if mth in [4, 6, 9, 11]:  # April, June, September, November
        return 0 < dy <= 30
    elif mth == 2:  # February
        return 0 < dy <= (29 if is_leap_year(yr) else 28)
    elif mth in [1, 3, 5, 7, 8, 10, 12]:
        return 0 < dy <= 31
    else:
        return False

# ---------- Day-of-week (Zeller) ----------

def calculate_weekday(day, month, year):
    # Assumes a valid Gregorian date
    if month < 3:
        month += 12
        year -= 1
    C = year // 100
    D = year % 100
    F = (day + (13 * (month + 1)) // 5 + D + D // 4 + C // 4 - 2 * C) % 7
    weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return weekdays[int(F)]

# ---------- Exact age calculator ----------

def calculate_exact_age(birthday, birthmonth, birthyear):
    today = date.today()

    year = today.year - birthyear
    month = today.month - birthmonth
    day = today.day - birthday

    # Borrow days from previous month if needed
    if day < 0:
        month -= 1
        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year
        day += days_in_month(prev_month, prev_year)

    # Borrow months from previous year if needed
    if month < 0:
        year -= 1
        month += 12

    return year, month, day

# ---------- Flask route ----------

@app.route('/', methods=['GET', 'POST'])
def index():
    weekday = None
    error = None

    leap_year_msg = None
    leap_error = None

    age_result = None
    age_error = None

    if request.method == 'POST':
        form_type = request.form.get('form_type')

        # ----- Day-of-week form -----
        if form_type == 'weekday':
            try:
                day = int(request.form['day'])
                month = int(request.form['month'])
                year = int(request.form['year'])

                if not check_valid_day(day):
                    error = "Invalid day!"
                elif not check_valid_day_in_month(month, day, year):
                    error = "Invalid date for that month!"
                else:
                    weekday = calculate_weekday(day, month, year)
            except (ValueError, KeyError):
                error = "Please enter valid numbers!"

        # ----- Leap year form -----
        elif form_type == 'leap':
            try:
                year = int(request.form['leap_year'])
                if is_leap_year(year):
                    leap_year_msg = f"{year} is a leap year."
                else:
                    leap_year_msg = f"{year} is not a leap year."
            except (ValueError, KeyError):
                leap_error = "Please enter a valid year!"

        # ----- Age form -----
        elif form_type == 'age':
            try:
                b_day = int(request.form['birth_day'])
                b_month = int(request.form['birth_month'])
                b_year = int(request.form['birth_year'])

                # Validate using datetime.date
                try:
                    birth_date = date(b_year, b_month, b_day)
                except ValueError:
                    age_error = "Invalid birth date entered!"
                else:
                    if birth_date > date.today():
                        age_error = "Birth date cannot be in the future!"
                    else:
                        y, m, d = calculate_exact_age(b_day, b_month, b_year)
                        age_result = f"{y} years, {m} months, {d} days"
            except (ValueError, KeyError):
                age_error = "Please enter valid numbers!"

    return render_template(
        'index.html',
        weekday=weekday,
        error=error,
        leap_year_msg=leap_year_msg,
        leap_error=leap_error,
        age_result=age_result,
        age_error=age_error
    )

if __name__ == '__main__':
    app.run(debug=True)
