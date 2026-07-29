## Overview

This is a learning project built using Python.

The Employee Management System is a database-driven application that manages employee records. Employee data is stored in a database and the application provides CRUD operations.

## Features

The system supports the following functionalities:

1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Export Employee Data to CSV
7. Exit

## Technologies Used

- Python
- SQLite Database
- SQL
- CSV File Handling
- Git & GitHub

## Project Structure

employee_management/
│
├── main.py # Application entry point
├── menu.py # User menu handling
├── employee.py # Employee operations
├── database.py # Database connection and queries
├── validation.py # Input validation functions
├── config.py # Configuration settings
│
├── database/
│ ├── create_DB.sql
│ └── select.sql
│
├── sql/
│ ├── create_tables.sql
│ ├── insert_employee.sql
│ ├── update_emp_data.sql
│ └── delete_emp_data.sql
│
├── logs/
│ └── .gitkeep
│
└── requirements.txt

## How to Run

1. Clone the repository

2. Create and activate a virtual environment

3. Install dependencies:

terminal

pip install -r requirements.txt

then run the below command to execute the application
python main.py