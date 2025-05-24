# Title: File Write, Read, and Text Processing
# Author: Rushikesh Padaki
# Date: 24 May 2025
#
# Description:
# A Python program that demonstrates basic file operations and string manipulations:
# - Writes user input (paragraph) to a text file named `my_file.txt`.
# - Reads the content from the file.
# - Displays:
#     • Original content
#     • Modified content (each word capitalized)
#     • Reversed content (character-wise)
#
# Algorithm:
# 1. Define function `write()`:
#    - Accept a paragraph from the user using input().
#    - Write the paragraph to `my_file.txt` using file write mode.
# 2. Define function `read()`:
#    - Open `my_file.txt` in read mode and read the content.
#    - Display the original content.
#    - Convert the content using `.title()` to capitalize the first letter of every word.
#    - Display the modified content.
#    - Reverse the modified string using slicing and display it.
# 3. Call `write()` followed by `read()` to demonstrate both functionalities.
#
# Time Complexity:
# - O(n) — where n is the number of characters in the paragraph.
#
# Space Complexity:
# - O(n) — to store original, modified, and reversed content.
#
# Sample Execution:
#
# Input:
# Enter the paragraph: hello world. this is a file operation demo.
#
# Output:
# ------------------------------
# Original Content
# ------------------------------
# hello world. this is a file operation demo.
#
# ------------------------------
# Modified Content
# ------------------------------
# Hello World. This Is A File Operation Demo.
#
# ------------------------------
# Reversed Content
# ------------------------------
# .omeD noitarepO eliF A sI sIhT .dlroW olleH

# Function to write content to the file
def write():
    string = input("Enter the paragraph: ")

    # Write content to file
    with open("my_file.txt", 'w') as file:
        file.write(string)

# Function to read and process the content
def read():
    # Read content from file
    with open("my_file.txt", 'r') as file:
        data = file.read()

    print("\n------------------------------")
    print("Original Content")
    print("------------------------------")
    print(data)

    # Capitalize the first letter of every word
    modified_data = data.title()

    print("\n------------------------------")
    print("Modified Content")
    print("------------------------------")
    print(modified_data)

    # Reverse the content (character-wise)
    print("\n------------------------------")
    print("Reversed Content")
    print("------------------------------")
    print(modified_data[::-1])

# Execute the functions
write()
read()
