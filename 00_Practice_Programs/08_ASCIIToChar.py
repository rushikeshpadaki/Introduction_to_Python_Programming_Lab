# Title: Character from ASCII Value
# Author: Rushikesh Padaki
# Date: 23 May 2025
#
# Description:
# A Python program to display the character corresponding to a given ASCII value.
# - Takes an integer input from the user representing the ASCII code.
# - Uses the built-in chr() function to convert it to the corresponding character.
# - Outputs a formatted message showing the result.
#
# Algorithm:
# 1. Prompt the user to enter an ASCII value as an integer.
# 2. Convert the ASCII value to a character using chr().
# 3. Display the character along with its corresponding ASCII value.
#
# Time Complexity:
# - O(1) — Constant time conversion and printing.
#
# Space Complexity:
# - O(1) — Only one integer and one character are stored.
#
# Sample Execution:
#
# Case 1: ASCII value 65
# Input:
# Enter the ASCII value of character: 65
# Output:
# The character associated with the ASCII value 65 is A
#
# Case 2: ASCII value 97
# Input:
# Enter the ASCII value of character: 97
# Output:
# The character associated with the ASCII value 97 is a

ascii_value = int(input('Enter the ASCII value of character: '))

print('The character associated with the ASCII value ' + str(ascii_value) + ' is ' + chr(ascii_value))
