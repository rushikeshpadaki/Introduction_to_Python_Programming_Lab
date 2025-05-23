# Title: Remove a Word from a String
# Author: Rushikesh Padaki
# Date: 23 May 2025
#
# Description:
# A Python program to remove all occurrences of a specified word from a user-provided string.
# - Takes input string and the word to remove from the user.
# - Uses the str.replace() method to replace all instances of the word with an empty string.
# - Displays the resulting modified string.
#
# Algorithm:
# 1. Prompt the user to enter a string and store it in 'text'.
# 2. Prompt the user to enter the word to remove and store it in 'word'.
# 3. Use text.replace(word, "") to remove all instances of the word from the string.
# 4. Print the modified string.
#
# Time Complexity:
# - O(n) — Where n is the length of the input string.
#
# Space Complexity:
# - O(n) — A new string is created after replacement.
#
# Sample Execution:
#
# Case 1: Remove 'is' from a sentence
# Input:
# Enter a string:
# this is a test string
# Enter a word to remove from the string:
# is
# Output:
# String after replacing: th  a test string

print('Enter a string:')
text = input()

print('Enter a word to remove from the string:')
word = input()

text = text.replace(word, "")

print('String after replacing: ' + text)
