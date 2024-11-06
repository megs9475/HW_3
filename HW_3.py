# Meghan Longua
# UWYO COSC 1010
# Submission Date: 11/5/2024
# HW 03
# Lab Section: 15
# Sources, people worked with, help given to: Wyatt Lohman, Abby Ferguson
# your
# comments
# here

def day_of_week(year, month, day):
    """Calculates the day of the week using Zeller's congruence."""

    if month < 3:
        month += 12
        year -= 1

    k = year % 100
    j = year // 100

    h = (day + (13 * (month + 1) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[h]

def main():
    date_str = input("Enter a date in MM/DD/YYYY format: ")
    month, day, year = map(int, date_str.split("/"))

    day_name = day_of_week(year, month, day)
    print(f"{date_str} is a {day_name}")

if __name__ == "__main__":
    main()
