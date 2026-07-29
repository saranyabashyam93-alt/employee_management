import database
import menu
import employee

print("hello")
try:
    database.initialize_database()
    print("database initialized successfully")
    while True:
        choice = menu.select_menu()
        print (f"You selected: {choice}")
        if choice == 1 :
            emp=employee.add_employee()
            print("Employee data added")
        elif choice == 2 :
            print("View Employee")
            emp=employee.view_all_employees()
        elif choice == 3 :
            print("Search Employee")
            emp=employee.search_employee()
        elif choice == 4 :
            print("Update Employee")
            emp=employee.update_employee()
        elif choice == 5 :
            print("Delete Employee")
            emp=employee.delete_employee()
        elif choice == 6 :
            print("Export CSV")
            emp=employee.export_csv()
        elif choice == 7 :
            print("Thank you for using Employee Management System.")
            break    
except Exception as e:
    print(f"ERROR: {e}")
    exit()

