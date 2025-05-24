# Title: Interactive List Operations Menu
# Author: Rushikesh Padaki
# Date: 24 May 2025
#
# Description:
# A Python program that performs various list operations using a menu-driven interface.
# - Accepts a list of integers from the user.
# - Provides a menu to:
#     1. Insert an element at a specific position
#     2. Remove an element from a specific position
#     3. Append an element to the end of the list
#     4. Display the current list
#     5. Exit the program
# - Includes input validation and loop until user chooses to exit.
#
# Algorithm:
# 1. Accept initial list of elements from the user.
# 2. Loop to display menu and perform chosen operation:
#    - Insert at specific index using list.insert(pos, item).
#    - Remove element using list.pop(pos).
#    - Append element using list.append(item).
#    - Display current list.
#    - Exit the program.
#
# Time Complexity (per operation):
# - Insertion at index: O(n)
# - Removal at index: O(n)
# - Append: O(1)
# - Display: O(n)
#
# Space Complexity:
# - O(n) — List stores n elements.
#
# Sample Execution:
#
# Input:
# Enter the number of elements: 3
# Enter 3 elements:
# Enter an element to be inserted in list: 10
# Enter an element to be inserted in list: 20
# Enter an element to be inserted in list: 30
# Initial list: [10, 20, 30]
#
# ===============MENU===============
# 1. Insertion at specific position
# 2. Remove an element from list
# 3. Insert an element to list
# 4. Display the list
# 5. Exit
#
# Choice: 1
# Enter the position (0-based index) to insert at: 1
# Enter the element to insert: 15
# Output: Element inserted. List is now: [10, 15, 20, 30]
#
# Choice: 2
# Enter the position (0-based index) to remove: 2
# Output: Element 20 removed. List is now: [10, 15, 30]
#
# Choice: 3
# Enter an element to add to the end of the list: 40
# Output: Element added. List is now: [10, 15, 30, 40]
#
# Choice: 4
# Output: The list is now: [10, 15, 30, 40]
#
# Choice: 6
# Output: Invalid choice! Please select from 1 to 5.
#
# Choice: 5
# Output: Exiting...

numbers = []

n = int(input('Enter the number of elements: '))
print('Enter %d elements:' % n)
while n > 0:
    i = int(input('Enter an element to be inserted in list: '))
    numbers.append(i)
    n -= 1
print('Initial list:', numbers)

while True:
    print('\n===============MENU===============')
    print('1. Insertion at specific position')
    print('2. Remove an element from list')
    print('3. Insert an element to list')
    print('4. Display the list')
    print('5. Exit')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        position = int(input('Enter the position (0-based index) to insert at: '))
        if 0 <= position <= len(numbers):
            item = int(input('Enter the element to insert: '))
            numbers.insert(position, item)
            print('Element inserted. List is now:', numbers)
        else:
            print('Invalid position!')

    elif choice == 2:
        if len(numbers) == 0:
            print('List is empty. Nothing to remove.')
        else:
            position = int(input('Enter the position (0-based index) to remove: '))
            if 0 <= position < len(numbers):
                removed = numbers.pop(position)
                print(f'Element {removed} removed. List is now:', numbers)
            else:
                print('Invalid position!')

    elif choice == 3:
        item = int(input('Enter an element to add to the end of the list: '))
        numbers.append(item)
        print('Element added. List is now:', numbers)

    elif choice == 4:
        print('The list is now:', numbers)

    elif choice == 5:
        print('Exiting...')
        break

    else:
        print('Invalid choice! Please select from 1 to 5.')
