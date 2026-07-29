def display_menu():
    print("=" * 35)  
    print("Employee Management System")
    print("=" * 35)
    print ("1. Add Employee")
    print ("2. View Employees")
    print ("3. Search Employee")
    print ("4. Update Employee")
    print ("5. Delete Employee")
    print ("6. Export CSV")
    print ("7. Exit")

def select_menu():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-7):"))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid option. Please choose between 1 and 7.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
