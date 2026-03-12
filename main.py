from employee import *

while True:

    print("\nEmployee Management System")

    print("1 Add Employee")
    print("2 View Employees")
    print("3 Update Employee")
    print("4 Delete Employee")
    print("5 Search Employee")
    print("6 Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employees()

    elif choice == 3:
        update_employee()

    elif choice == 4:
        delete_employee()

    elif choice == 5:
        search_employee()

    elif choice == 6:
        break

    else:
        print("Invalid Choice")