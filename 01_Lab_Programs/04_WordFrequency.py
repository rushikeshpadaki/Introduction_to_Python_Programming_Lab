# Title: Paragraph Word Count and Frequency Analyzer
# Author: Rushikesh Padaki
# Date: 24 May 2025
#
# Description:
# A Python program that:
# - Accepts a paragraph from the user (terminated by an empty line).
# - Joins all lines to form a full paragraph.
# - Splits the paragraph into words and calculates:
#     • Total word count
#     • Frequency of each unique word
# - Also searches for the presence of a user-specified word within the paragraph.
#
# Algorithm:
# 1. Prompt the user to input lines for the paragraph, ending with a blank line.
# 2. Combine the lines using `' '.join()` to form a single string.
# 3. Split the paragraph into individual words using `.split()`.
# 4. Count the total number of words.
# 5. Use a dictionary to count frequency of each word.
# 6. Display the word-frequency dictionary.
# 7. Prompt the user to input a word and check if it exists in the paragraph using `.find()`.
#
# Time Complexity:
# - O(n) — where n is the number of words for counting and searching.
#
# Space Complexity:
# - O(n) — dictionary stores each unique word and its frequency.
#
# Sample Execution:
#
# Case 1: Word is present
# Input:
# Enter a paragraph (Press ENTER twice to end):
# Python is powerful.
# Python is easy to learn.
#
# Output:
# Entered paragraph:
# Python is powerful. Python is easy to learn.
# Number of words: 8
# Word frequency:
# Python: 2
# is: 2
# powerful.: 1
# easy: 1
# to: 1
# learn.: 1
# Enter a word to search: Python
# Word found in paragraph!!
#
# Case 2: Word is not present
# Input:
# Enter a paragraph (Press ENTER twice to end):
# Data science is an evolving field.
# It involves statistics and programming.
#
# Output:
# Entered paragraph:
# Data science is an evolving field. It involves statistics and programming.
# Number of words: 10
# Word frequency:
# Data: 1
# science: 1
# is: 1
# an: 1
# evolving: 1
# field.: 1
# It: 1
# involves: 1
# statistics: 1
# and: 1
# programming.: 1
# Enter a word to search: Python
# Word not found in the paragraph!

print('Enter a paragraph (Press ENTER twice to end):')
paragraph = []
while True:
    line = input()
    if line == '':
        break
    paragraph.append(line)

# Join the list of lines into a single string
full_paragraph = ' '.join(paragraph)
print('Entered paragraph:\n', full_paragraph)

# Split into words
words = full_paragraph.split()
wordCount = len(words)
print('Number of words:', wordCount)

# Count word frequencies
count = dict()
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print('Word frequency:')
for word, freq in count.items():
    print(f'{word}: {freq}')

# Search for a word in the paragraph
searchWord = input('Enter a word to search: ')
result = full_paragraph.find(searchWord)
if result == -1:
    print('Word not found in the paragraph!')
else:
    print('Word found in paragraph!!')
