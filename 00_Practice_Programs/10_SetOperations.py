# Title: Set Operations in Python
# Author: Rushikesh Padaki
# Date: 23 May 2025
#
# Description:
# A Python program to demonstrate basic set operations:
# - Union
# - Intersection
# - Difference
# - Symmetric Difference
# - The sets A and B are statically defined using Python's built-in set data structure.
#
# Algorithm:
# 1. Define two sets A and B.
# 2. Use set operators:
#    - Union (A | B) combines all elements from both sets.
#    - Intersection (A & B) finds elements common to both sets.
#    - Difference (A - B) finds elements in A but not in B.
#    - Symmetric Difference (A ^ B) finds elements in A or B but not both.
# 3. Print the result of each operation.
#
# Time Complexity:
# - O(n) — Each operation is linear in the size of the sets.
#
# Space Complexity:
# - O(n) — Output sets require additional space.
#
# Sample Execution:
#
# Case 1:
# Output:
# Union of Sets A and B :  {0, 1, 2, 3, 4, 5, 6, 8}
# Intersection of Sets A and B :  {2, 4}
# Difference of Sets A and B :  {0, 8, 6}
# Symmetric difference of Sets A and B :  {0, 1, 3, 5, 6, 8}

A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

print('Union of Sets A and B : ', A | B)
print('Intersection of Sets A and B : ', A & B)
print('Difference of Sets A and B : ', A - B)
print('Symmetric difference of Sets A and B : ', A ^ B)
