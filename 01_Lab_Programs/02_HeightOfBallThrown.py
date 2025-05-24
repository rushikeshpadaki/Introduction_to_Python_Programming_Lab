# Title: Maximum Height of a Thrown Ball
# Author: Rushikesh Padaki
# Date: 24 May 2025
#
# Description:
# A Python program to compute the maximum height reached by a ball thrown vertically upward.
# - Takes initial velocity (u) and the height of the person (h₀) as inputs.
# - Uses standard equations of motion from physics:
#     • Time to reach max height: t = -u / a
#     • Maximum height above hand: h = ut + 0.5 * a * t²
#     • Total height from ground = h₀ + h
# - Acceleration due to gravity is taken as a = -9.8 m/s² (acting downward).
#
# Algorithm:
# 1. Define acceleration due to gravity `a = -9.8 m/s²`.
# 2. Take input for initial velocity `u` and height of the person `h₀`.
# 3. Compute time to reach maximum height: t = -u / a.
# 4. Compute max height above the hand using: h = ut + 0.5at².
# 5. Add h₀ to get total height from the ground.
# 6. Print all results rounded to 5 decimal places.
#
# Time Complexity:
# - O(1) — Constant time for calculations.
#
# Space Complexity:
# - O(1) — Constant space for variables.
#
# Sample Execution:
#
# Case 1:
# Input:
# Enter the initial velocity (in m/s): 10
# Enter the height of the person (in meters): 1.6
# Output:
# The time taken for the ball to reach maximum height:  1.02041  seconds
# The maximum height the ball reached (above hand):  5.10204  meters
# The total height of the ball from ground:  6.70204  meters

a = -9.8  # Acceleration due to gravity in m/s^2

b = float(input('Enter the initial velocity (in m/s): '))
pHeight = float(input('Enter the height of the person (in meters): '))

# Time to reach max height
t = -b / a
print('The time taken for the ball to reach maximum height: ', round(t, 5), ' seconds')

# Maximum height above the person's hand
h = b * t + 0.5 * a * t ** 2
print('The maximum height the ball reached (above hand): ', round(h, 5), ' meters')

# Total height from ground
totalHeight = h + pHeight
print('The total height of the ball from ground: ', round(totalHeight, 5), ' meters')
