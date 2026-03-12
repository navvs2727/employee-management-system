# Employee Management System (Python + MySQL)

A simple and efficient **Employee Management System** built using **Python and MySQL**.
This project demonstrates the implementation of **CRUD operations** with database integration.

The system allows users to manage employee records such as adding new employees, viewing employee details, updating information, and deleting records.

---

## Features

* Add New Employee
* View All Employees
* Update Employee Details
* Delete Employee Record
* Search Employee by ID
* MySQL Database Integration

---

## Technologies Used

* **Python**
* **MySQL**
* **mysql-connector-python**
* **CRUD Operations**
---

## Project Structure

Employee-Management-System


 - database.py       → Database connection
 - employee.py       → Employee CRUD functions
 - main.py           → Main program
 - requirements.txt  → Required libraries
 - README.md         → Project documentation

---

##  Installation & Setup

- Clone the repository

git clone https://github.com/yourusername/employee-management-system.git

- Go to project folder

cd employee-management-system

- Install required library

pip install mysql-connector-python

- Setup MySQL database

Create database and table:

CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE employees(
emp_id INT PRIMARY KEY,
name VARCHAR(50),
department VARCHAR(50),
salary INT
);

- Run the project

python main.py

---

## Example Menu

Employee Management System

1 Add Employee
2 View Employees
3 Update Employee
4 Delete Employee
5 Search Employee
6 Exit

---

## Future Improvements

* Login Authentication System
* GUI Version using Tkinter
* Export data to CSV/Excel
* Employee Salary Analytics

---

## Author

**Navneet Singh**
Python Developer
---
