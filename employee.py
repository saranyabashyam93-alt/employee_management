import validation
import database
import csv
import config
from pathlib import Path

def add_employee():
    print("enter below the employee details")
##   first_name = input("Enter First Name : ")
##   last_name  = input("Enter Last Name: ")
##   email      = input("Enter Email: ")
##   phone_num  = input("Enter Phone Number:")
##   department = input("Enter Department:")
##   designation = input("Enter Designation:")
##   salary     = input("Enter Salary:")
##   join_date  =input("Enter Joining Date:")
    while True:
        is_valid = True
        return_message = None
        in_fname= input("Enter First Name : ").strip()
        in_fname.capitalize()
        is_valid,return_message = validation.validate_first_name(in_fname)
        if is_valid:
            break
        print(return_message)
    while True:
        is_valid = True
        return_message = None
        in_lname = input("Enter Last Name : ").strip()
        in_lname.capitalize()
        is_valid,return_message  = validation.validate_last_name(in_lname)
        if is_valid:
            break
        print(return_message)
    while True:
        is_valid = True
        return_message = None
        in_emailid = input("Enter a Email Id : ").strip()
        in_emailid.lower()
        is_valid,return_message= validation.validate_email(in_emailid)
        if is_valid:
            break
        print(return_message)
    while True:
        is_valid = True
        return_message = None
        in_phonenum  = input("Enter a 10 digit Phone Number:").strip()
        in_phonenum  = in_phonenum.replace(" ","")
        in_phonenum  = in_phonenum.replace("-","")
        is_valid, return_message  = validation.validate_phonenum(in_phonenum)
        if is_valid:
            break
        print(return_message)
    while True:
        is_valid = True
        return_message = None
        in_dept= input("enter the employees department:").strip()
        is_valid, return_message= validation.validate_department(in_dept)
        if is_valid:
             break
        print(return_message)
    while True:
        is_valid = True
        return_message= None
        in_desgination=input("enter the employees designation:").strip()
        in_desgination.capitalize()
        is_valid,return_message= validation.validate_designation(in_desgination)
        if is_valid:
            break
        print(return_message)
    while True:
        is_valid = True
        return_message= None
        try:
            in_salary=float(input("enter salary :"))
            is_valid, return_message = validation.validate_salary(in_salary)
            if is_valid:
                break
            print(return_message)
        except ValueError:
            print("salary must be numeric")
            continue
        
    while True:
        is_valid= True
        return_message = None
        in_join_date=input("enter the employee's Joining date (yyyy-mm-dd):").strip()
        is_valid,return_message  = validation.validate_join_date(in_join_date)
        if is_valid:
            join_date = return_message
            break
        print(return_message)
    emp_data={"First_Name" : in_fname,
              "Last_Name"  : in_lname,
              "Email"      : in_emailid,
              "Phone"      : in_phonenum,
              "Department" : in_dept,
              "Designation": in_desgination,
              "Salary"     : in_salary,
              "Joining_Date" : join_date} 
    print(emp_data)
    insert_db=database.Insert_employee(emp_data)
    print(insert_db)

def view_all_employees():
    view_db,_= database.get_all_employees()
    if len(view_db) == 0 :
        print("No employees found.")
    else:
        print("*" *20)
        print("employees details")
        print(f"total employees: {len(view_db)}")
        for row in view_db:
            display_record(row)
        
def search_employee():
    print("starting search employee")
    while True:
        try:
            emp_id=int(input("enter the employee id:"))
            if emp_id <= 0:
                print("invalid. employee id should be greater than zero")
                continue
            else:
                search=database.get_employee_byempid(emp_id)
                if search:
                    print("*" *20)
                    print("employee details")
                    print(f"for employee id {emp_id}")            
                    display_record(search)
                    break
                else:
                    print("employee details not found")
                    break
        except ValueError:
            print("invalid.. please enter only number")
            continue

def display_record(row):  
    Employee_ID, First_Name, Last_Name, Email, Phone, Department, Designation, Salary, Joining_Date = row
    print("*" *20)   
    print(f"Employee_ID: {Employee_ID}")    
    print(f"First_Name: {First_Name}")
    print(f"Last_Name:{Last_Name}")  
    print(f"Email: {Email}") 
    print(f"Phone: {Phone}")
    print(f"Department: {Department}") 
    print(f"Designation: {Designation}") 
    print(f"Salary: {Salary}")
    print(f"Joining_Date: {Joining_Date}")
    print("*" *20)

def update_employee():
    while True:
        try:
            emp_id=int(input("enter the employee id you want to update:"))
            if emp_id <= 0:
                print("invalid. employee id should be greater than zero")
                continue
            else:
                search=database.get_employee_byempid(emp_id)
                if search:
                    print("*" *20)
                    print("Current Employee")         
                    display_record(search)
                    print("Press Enter to keep the current value.")
                    _,First_Name, Last_Name, Email, Phone, Department, Designation, Salary, Joining_Date = search
                    prompt="First_Name"
                    function_name="validate_first_name"
                    fname_u=get_update_value(prompt,First_Name,function_name,"First_Name")
                    prompt="Last_Name"
                    function_name="validate_last_name"
                    lname_u=get_update_value(prompt,Last_Name,function_name,"Last_Name")
                    prompt="Email"
                    function_name="validate_email"
                    email_u=get_update_value(prompt,Email,function_name,"Email")
                    prompt="Phone"
                    function_name="validate_phonenum"
                    phone_u=get_update_value(prompt,Phone,function_name,"Phone")
                    prompt="Department"
                    function_name="validate_department"
                    dept_u=get_update_value(prompt,Department,function_name,"Department")
                    prompt="Designation"
                    function_name="validate_designation"
                    desig_u=get_update_value(prompt,Designation,function_name,"Designation")
                    prompt="Salary"
                    function_name="validate_salary"
                    salary_u=get_update_value(prompt,Salary,function_name,"Salary")
                    prompt="Joining_Date"
                    function_name="validate_join_date"
                    join_date_u=get_update_value(prompt,Joining_Date,function_name,"Joining_Date")
                    upd_emp_data = { "First_Name" : fname_u,
                                      "Last_Name"  : lname_u,
                                      "Email"      : email_u,
                                      "Phone"      : phone_u,
                                      "Department" : dept_u,
                                      "Designation": desig_u,
                                      "Salary"     : salary_u,
                                      "Joining_Date" : join_date_u}
                    update_db=database.update_employee(upd_emp_data,emp_id)
                    print(update_db)
                    break
                else:
                    print("employee details not found")
                    break
        except ValueError as e:
            print("invalid.. please enter only number:",e)
            continue

def get_update_value(prompt,current_value,function_name,field_name):
    while True:
        try:
            in_value=input(f"{prompt} [{current_value}] : ").strip()
            if field_name == "First_Name":
                in_value=in_value.capitalize()
            elif field_name == "Last_Name":
                in_value=in_value.capitalize()
            elif field_name == "Email":
                in_value=in_value.lower()
            elif field_name == "Phone":
                in_value=in_value.replace(" ","")
                in_value=in_value.replace("-","")
            elif field_name == "Designation":
                in_value=in_value.capitalize()

            if in_value != "":
                if field_name == "Salary":
                    in_value=float(in_value)
                is_valid = True
                return_message = None
                validator=getattr(validation,function_name)
                is_valid,return_message = validator(in_value)
                if is_valid:
                    if field_name == "Joining_Date":
                        in_value = return_message
                    return in_value
                print(return_message)
            else:
                in_value= current_value
                return in_value
        except Exception as e:
            print("get_update_value:", e )
            break

def delete_employee():
    while True:
        try:
            in_empid=int(input("enter the emp id to delete:"))
            if in_empid <= 0 :
                print("invalid. employee id should be greater than zero")
            else:
                search=database.get_employee_byempid(in_empid)
                if search:
                    print("*" *20)
                    print("Current details of Employee id:",in_empid) 
                    display_record(search)
                    while True:
                        print("Are you sure you want to delete this employee?")
                        confirm=input("Y or N:").strip()
                        confirm=confirm.upper()
                        if confirm == "Y":
                            delete=database.delete_employee(in_empid)
                            if delete == 0:
                                print("Employee not found / already deleted")
                            else:
                                print("successfully employee data deleted")
                            break
                        elif confirm == "N":
                            print("cancelled delete")
                            break
                        else:
                            print("Invalid option. Please enter Y or N.")
                            continue
                    break
                else:
                    print("employee details not found")
                    break
        except ValueError as e:
            print("invalid.. please enter only number:",e)
            continue

def export_csv():
    emp_data,header=database.get_all_employees()
    if len(emp_data) == 0:
        print("No employees to export.")
    else:
        folder=Path.home() / "Desktop" / "saranya_python" / "employee_exports"
        folder.mkdir(exist_ok=True)
        csvfile=folder / "employees.csv"
        with open(csvfile,"w",newline="",encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow(header)
            for row in emp_data:
                writer.writerow(row)
        print(f"total employee exported : {len(emp_data)}")




