# M02 Lab - Case Study: if...else and while
# author: Kris McIntosh
# created: 2023-01-26  updated: 2023-01-26 (Kris McIntosh)
# A program that uses the variables if, else and while.

# Use while to repeat until 5 names are entered.
while True:
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    if gpa >= 3.5:
        print(first_name + " " + last_name + " has made the Dean's List!")
    elif gpa >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll!")
