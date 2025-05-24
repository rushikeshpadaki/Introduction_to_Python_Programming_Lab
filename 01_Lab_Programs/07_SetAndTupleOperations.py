# Title: Set and Tuple Operations Menu
# Author: Rushikesh Padaki
# Date: 24 May 2025
#
# Description:
# A Python program that provides a menu-based interface to perform operations on sets and tuples.
# - Users can choose to perform:
#     • Set Operations: Add, Remove, Update (multiple), Display
#     • Tuple Operations: Add (append), Delete (clear), Display
#     • Exit from each menu or entire program
# - Demonstrates immutability of tuples and dynamic nature of sets.
#
# Algorithm:
# 1. Initialize an empty set and tuple.
# 2. Display a main menu with options for set, tuple, or exit.
# 3. Based on the user’s selection:
#    - For Set:
#        - Add element using set.add()
#        - Remove element using set.discard()
#        - Update set with multiple values using set.update()
#        - View set contents
#    - For Tuple:
#        - Append by reassigning using tuple += (element,)
#        - Clear tuple by reassigning to ()
#        - View tuple contents
# 4. Validate all user inputs and loop until termination.
#
# Time Complexity:
# - Set Operations:
#     Add/Remove/Update/Display: O(1) average per element
# - Tuple Operations:
#     Add (append): O(n), as new tuple is created
#     Delete: O(1)
#     Display: O(n)
#
# Space Complexity:
# - O(n) for both set and tuple to store elements
#
# Sample Execution:
#
# Input:
# Enter your choice
# S : Set Operation
# T : Tuple Operation
# N : Terminate
# s
#
# Choose the Set operation
# 1 : Add/Insert
# 2 : Remove/Delete
# 3 : Update/Append
# 4 : Display/View
# 0 : Exit
# Enter operation number: 1
# Enter the element to add: apple
# Updated Set: {'apple'}
#
# Enter operation number: 3
# Enter multiple elements to update (comma separated): banana,grape
# Updated Set: {'banana', 'apple', 'grape'}
#
# Enter operation number: 0
#
# Enter your choice
# S : Set Operation
# T : Tuple Operation
# N : Terminate
# t
#
# Choose the Tuple operation
# 1 : Add/Insert
# 2 : Delete Tuple
# 3 : Display/View
# 0 : Exit
# Enter operation number: 1
# Enter the element to add: mango
# Updated Tuple: ('mango',)
#
# Enter operation number: 2
# Tuple Deleted.
#
# Enter your choice
# S : Set Operation
# T : Tuple Operation
# N : Terminate
# n
# Program terminated.

# Create empty set and tuple
setdata = set()
tupledata = tuple()

# Run infinite loop for menu
while True:
    choice = input("Enter your choice\nS : Set Operation\nT : Tuple Operation\nN : Terminate\n").lower()

    if choice == 's':
        while True:
            print("\nChoose the Set operation")
            print("1 : Add/Insert")
            print("2 : Remove/Delete")
            print("3 : Update/Append")
            print("4 : Display/View")
            print("0 : Exit")

            operations = int(input("Enter operation number: "))

            if operations == 1:
                data = input("Enter the element to add: ")
                setdata.add(data)
                print("Updated Set:", setdata)

            elif operations == 2:
                data = input("Enter the element to delete: ")
                setdata.discard(data)
                print("Updated Set:", setdata)

            elif operations == 3:
                data_list = input("Enter multiple elements to update (comma separated): ").split(',')
                setdata.update(data_list)
                print("Updated Set:", setdata)

            elif operations == 4:
                print("Current Set:", setdata)

            elif operations == 0:
                break

            else:
                print("Invalid Choice. Try again.")

    elif choice == 't':
        while True:
            print("\nChoose the Tuple operation")
            print("1 : Add/Insert")
            print("2 : Delete Tuple")
            print("3 : Display/View")
            print("0 : Exit")

            operations = int(input("Enter operation number: "))

            if operations == 1:
                data = input("Enter the element to add: ")
                tupledata += (data,)  # Append as a new element
                print("Updated Tuple:", tupledata)

            elif operations == 2:
                tupledata = ()
                print("Tuple Deleted.")

            elif operations == 3:
                print("Current Tuple:", tupledata)

            elif operations == 0:
                break

            else:
                print("Invalid Choice. Try again.")

    elif choice == 'n':
        print("Program terminated.")
        break

    else:
        print("Invalid Choice! Please enter 'S', 'T', or 'N'.")
