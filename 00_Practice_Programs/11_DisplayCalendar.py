# Title: Display Calendar for a Given Month and Year
# Author: Rushikesh Padaki
# Date: 23 May 2025
#
# Description:
# A Python program to display the calendar for a specific month and year entered by the user.
# - Utilizes the built-in `calendar` module.
# - Accepts year and month as input.
# - Displays a formatted calendar for the specified month.
#
# Algorithm:
# 1. Import the `calendar` module.
# 2. Prompt the user to enter the year and month.
# 3. Use `calendar.month(year, month)` to get a string representation of the month's calendar.
# 4. Print the result.
#
# Time Complexity:
# - O(1) — Calendar generation is fixed for given input.
#
# Space Complexity:
# - O(1) — The output string is of constant size for a single month.
#
# Sample Execution:
#
# Case 1:
# Input:
# Enter year: 2025
# Enter month: 5
# Output:
#       May 2025
# Mo Tu We Th Fr Sa Su
#           1  2  3  4
#  5  6  7  8  9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30 31

import calendar

YEAR = int(input('Enter year: '))
MONTH = int(input('Enter month: '))

print(calendar.month(YEAR, MONTH))
