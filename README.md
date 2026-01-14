# Date Utilities Flask App

A simple Flask web application that provides three date-related tools:

- Day of the week calculator (using Zeller’s congruence)
- Leap year checker (Gregorian calendar)
- Exact age calculator (in years, months, and days)

---

## Features

### 1. Day of the Week Calculator
Input a valid Gregorian Calender date (day, month, year), and the website will compute the day of the week using Zeller’s congruence and displays it (Monday-Sunday).

### 2. Leap Year Checker
Input a year, and the website checks whether it is a leap year using the standard Gregorian rules:

- A year is a leap year if it is divisible by 4 and not by 100, **or**
- It is divisible by 400.

### 3. Exact Age Calculator
Given a birth date (day, month, year), the websites find out your exact age in days, months, years:

- Validates the date.
- Ensures the birth date is not in the future.
- Computes the exact age as years, months, and days relative to today.

---

## Project Structure

```text
project/
├─ app.py
└─ templates/
   └─ index.html
