# Title: Employee Database Management System
# Author: Rushikesh Padaki
# Date: 24 May 2025
#
# Description:
# A menu-driven Python program to manage employee records using a dictionary.
# - Employee details are stored as: key = Employee ID, value = [Name, DOB, Designation]
# - Provides functionality to:
#     1. Create multiple employee records at once
#     2. Add a single employee
#     3. Search for an employee by ID
#     4. Delete an employee by ID
#     5. Display all employee records
#     6. Exit the program
#
# Algorithm:
# 1. Use a dictionary `Employee` to store employee data.
# 2. Display menu and prompt the user to choose an operation.
# 3. Based on the choice:
#    - (1) Create multiple employees by accepting details in a loop.
#    - (2) Add a single employee.
#    - (3) Search using Employee.get(ID).
#    - (4) Delete using Employee.pop(ID).
#    - (5) Traverse dictionary and print each record.
#    - (6) Exit the loop.
# 4. Validate user input for menu and ID presence.
#
# Time Complexity:
# - Insert/Search/Delete: O(1) on average for dictionary operations.
#
# Space Complexity:
# - O(n) — Where n is the number of employees stored.
#
# Sample Execution:
#
# ====== Employee Database ======
# 1. Create Employees
# 2. Add New Employee
# 3. Search Employee
# 4. Delete Employee
# 5. Display All Employees
# 6. Exit
# ===============================
#
# Enter your choice: 1
# Enter the number of employees: 2
# Enter details for Employee 1
# Enter the Employee ID: 101
# Enter the Employee Name: Alice
# Enter the DOB (dd-mm-yyyy): 01-01-1990
# Enter the Designation: Manager
#
# Enter details for Employee 2
# Enter the Employee ID: 102
# Enter the Employee Name: Bob
# Enter the DOB (dd-mm-yyyy): 15-05-1992
# Enter the Designation: Developer
#
# Employee added successfully.
#
# Choice: 3
# Enter the Employee ID to search: 101
# Employee Found: ID 101, Details: ['Alice', '01-01-1990', 'Manager']
#
# Choice: 4
# Enter the Employee ID to delete: 102
# Employee deleted successfully.
#
# Choice: 5
# Current Employee Database:
# ID: 101 -> Name: Alice, DOB: 01-01-1990, Designation: Manager
#
# Choice: 6
# Exiting...

# Creating the Dictionary
Employee = dict()

while True:
    print('\n====== Employee Database ======\n')
    print('1. Create Employees')
    print('2. Add New Employee')
    print('3. Search Employee')
    print('4. Delete Employee')
    print('5. Display All Employees')
    print('6. Exit')
    print('===============================\n')

    Choice = int(input('Enter your choice: '))

    if Choice == 1:
        n = int(input('Enter the number of employees: '))
        for i in range(n):
            print('--------------------------------')
            print(f'Enter details for Employee {i + 1}')
            print('--------------------------------')
            EmpId = int(input('Enter the Employee ID: '))

            EmpDetails = []
            EmpName = input('Enter the Employee Name: ')
            EmpDOB = input('Enter the DOB (dd-mm-yyyy): ')
            Designation = input('Enter the Designation: ')

            EmpDetails.extend([EmpName, EmpDOB, Designation])
            Employee[EmpId] = EmpDetails
            print('Employee added successfully.\n')

    elif Choice == 2:
        EmpId = int(input('Enter the Employee ID: '))

        EmpDetails = []
        EmpName = input('Enter the Employee Name: ')
        EmpDOB = input('Enter the DOB (dd-mm-yyyy): ')
        Designation = input('Enter the Designation: ')

        EmpDetails.extend([EmpName, EmpDOB, Designation])
        Employee[EmpId] = EmpDetails
        print('Employee added successfully.\n')

    elif Choice == 3:
        EId = int(input('Enter the Employee ID to search: '))
        emp = Employee.get(EId)
        if emp:
            print('--------------------------------')
            print(f'Employee Found: ID {EId}, Details: {emp}')
            print('--------------------------------')
        else:
            print('Employee not found!')

    elif Choice == 4:
        EId = int(input('Enter the Employee ID to delete: '))
        if EId in Employee:
            Employee.pop(EId)
            print('Employee deleted successfully.')
        else:
            print('Employee ID not found.')

    elif Choice == 5:
        if not Employee:
            print('\nNo employee details found.\n')
        else:
            print('\nCurrent Employee Database:')
            for key, value in Employee.items():
                print(f'ID: {key} -> Name: {value[0]}, DOB: {value[1]}, Designation: {value[2]}')

    elif Choice == 6:
        print('Exiting...')
        break

    else:
        print('Invalid choice! Please select a valid option (1-6).')
