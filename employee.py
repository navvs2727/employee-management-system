from database import cursor, db

# Add Employee
def add_employee():
    emp_id = int(input("Enter Employee ID: "))

    cursor.execute("SELECT * FROM employees WHERE emp_id=%s",(emp_id,))
    if cursor.fetchone():
        print("Employee already exists")
        return

    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    cursor.execute(
        "INSERT INTO employees VALUES(%s,%s,%s,%s)",
        (emp_id,name,dept,salary)
    )
    db.commit()

    print("Employee Added Successfully")


# View Employees
def view_employees():
    cursor.execute("SELECT * FROM employees")

    data = cursor.fetchall()

    print("\nEmployee Records\n")

    for row in data:
        print(row)


# Update Employee
def update_employee():

    emp_id = int(input("Enter Employee ID to update: "))

    salary = int(input("Enter new salary: "))

    cursor.execute(
        "UPDATE employees SET salary=%s WHERE emp_id=%s",
        (salary,emp_id)
    )

    db.commit()

    print("Employee Updated")


# Delete Employee
def delete_employee():

    emp_id = int(input("Enter Employee ID to delete: "))

    cursor.execute(
        "DELETE FROM employees WHERE emp_id=%s",
        (emp_id,)
    )

    db.commit()

    print("Employee Deleted")


# Search Employee
def search_employee():

    emp_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "SELECT * FROM employees WHERE emp_id=%s",
        (emp_id,)
    )

    data = cursor.fetchone()

    if data:
        print(data)
    else:
        print("Employee Not Found")