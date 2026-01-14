# Date Utilities Flask App

A simple Flask web application that provides three date-related tools:

- Day of the week calculator (using Zeller’s congruence)
- Leap year checker (Gregorian calendar)
- Exact age calculator (in years, months, and days)

---

## Features

### 1. Day of the Week Calculator
The user inputs a valid Gregorian Calendar date (day, month, year), and the app will compute and display the day of the week (Monday-Sunday) using Zeller’s congruence formula. 

- Validates the date that is inputted
- Validates the date based on month as some months have different # of days
- Validates leap years using Gregorian rules
- Computes day of the week from the inputted date using Zeller's Congruence Formula


### 2. Leap Year Checker
The user inputs a year, and the app checks whether it is a leap year or not using the Gregorian rules:

- A year is a leap year if it is divisible by 4 and not by 100, **or**
- It is divisible by 400.

### 3. Elapsed Time/Exact Age Calculator
The user inputs a date (day, month, year), and the app will find out the how long ago the date was in days, months, years:

- Can also be used for birth dates to find out how exactly old the user is.
- Validates the date.
- Ensures the date is not in the future.
- Computes the exact age as years, months, and days relative to today.

---

## Project Structure

```text
project/
├─ app.py
└─ templates/
   └─ index.html
