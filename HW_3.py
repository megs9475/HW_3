# Meghan Longua
# UWYO COSC 1010
# Submission Date: 11/5/2024
# HW 03
# Lab Section: 15
# Sources, people worked with, help given to: Wyatt Lohman, Abby Ferguson
# your
# comments
# here

def date(year, month, day):
    
    if month < 3:
        month += 12
        year -= 1

    y = year % 100
    z = year // 100

    x = (day + (13 * (month + 1) // 5) + y + (y // 4) + (z // 4) - (2 * z)) % 7

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[x]

def date_with_weekday():
    date_str = input("Please input a date (MM/DD/YYYY): ")
    month, day, year = map(int, date_str.split("/"))

    day_name = date(year, month, day)
    print(f"{date_str} is a {day_name}")

if __name__ == "__date_with_weekday__":
    date_with_weekday()
