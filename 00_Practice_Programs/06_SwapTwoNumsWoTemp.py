# Title: Swap Two Numbers Using Tuple Unpacking
# Author: Rushikesh Padaki
# Date: 23 May 2025
#
# Description:
# A Python program to swap the values of two variables using tuple unpacking.
# - Demonstrates Pythonic way of swapping without using a temporary variable.
# - Takes integer inputs from the user.
# - Uses simultaneous assignment (x, y = y, x) for efficient swapping.
#
# Algorithm:
# 1. Accept input values for x and y from the user.
# 2. Display the values before swapping.
# 3. Use tuple unpacking to swap the values: x, y = y, x.
# 4. Display the values after swapping.
#
# Time Complexity:
# - O(1) — Constant time operations for assignment and printing.
#
# Space Complexity:
# - O(1) — No extra space is used as swapping is done in-place.
#
# Sample Execution:
#
# Case 1: Swap values of 5 and 8
# Input:
# Enter the value of x: 5
# Enter the value of y: 8
# Output:
# Before swapping:
# x =  5
# y =  8
# After swapping:
# x =  8
# y =  5

x = int(input('Enter the value of x: '))
y = int(input('Enter the value of y: '))

print('Before swapping:')
print('x = ', x)
print('y = ', y)

x, y = y, x

print('After swapping:')
print('x = ', x)
print('y = ', y)
