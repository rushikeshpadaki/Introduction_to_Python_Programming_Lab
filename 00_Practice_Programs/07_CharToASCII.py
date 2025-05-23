# Title: ASCII Value of a Character
# Author: Rushikesh Padaki
# Date: 23 May 2025
#
# Description:
# A Python program to find the ASCII value of a user-entered character.
# - Takes a single character input from the user.
# - Uses the built-in ord() function to obtain its ASCII value.
# - Displays the result with a descriptive message.
#
# Algorithm:
# 1. Prompt the user to input a character.
# 2. Use ord() to get the ASCII value of the character.
# 3. Print the character along with its ASCII value.
#
# Time Complexity:
# - O(1) — Constant time lookup using the ord() function.
#
# Space Complexity:
# - O(1) — Only one character and integer value are stored.
#
# Sample Execution:
#
# Case 1: Character 'A'
# Input:
# Enter a character: A
# Output:
# The ASCII value of character "A" is  65
#
# Case 2: Character 'z'
# Input:
# Enter a character: z
# Output:
# The ASCII value of character "z" is  122

character = input('Enter a character: ')

print('The ASCII value of character "' + character + '" is ', ord(character))
