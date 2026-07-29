import sqlite3
import config

def create_connection():
    connection = sqlite3.connect(config.DB_NAME)
    return connection

def initialize_database():
    connection = None
    cursor = None
    print ("hello database")
    try:  
        connection = create_connection()
        with open(config.CREATE_EMPLOYEES_TABLE,"r",encoding="utf-8") as file:
           sql_script = file.read()
        cursor = connection.cursor()
        cursor.execute(sql_script)
        print("here iam initialize_database")
        connection.commit()
    except sqlite3.Error as e:
        print("sql error:",e)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def DB_email_check(email_id):
    connection = None
    cursor = None
    DB_check = False
    print ("hello database")
    try:  
        connection = create_connection()
        with open(config.QUERY_EMPLOYEE_EMAIL,"r",encoding="utf-8") as file:
           sql_script = file.read()
        cursor = connection.cursor()
        cursor.execute(sql_script,(email_id,))
        row = cursor.fetchone()
        if row:
            DB_check = True
        return(DB_check)
    except sqlite3.Error as e:
        print("sql error:",e)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def Insert_employee(emp_data):
    connection=None
    cursor=None
    try:
        connection=create_connection()
        with open(config.INSERT_EMPLOYEE,"r",encoding="utf-8") as file:
            open_script=file.read()
        cursor=connection.cursor()
        values=(emp_data["First_Name"], 
               emp_data["Last_Name"], 
               emp_data["Email"], 
               emp_data["Phone"],
               emp_data["Department"], 
               emp_data["Designation"], 
               emp_data["Salary"], 
               emp_data["Joining_Date"])
        cursor.execute(open_script,values)
        print("here iam in Insert_employee")
        connection.commit()
        return("success insert")
    except sqlite3.Error as e:
        print("sql error:",e)
        return ("insert failed")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def get_all_employees():
    connection = None
    cursor = None
    try:
        connection = create_connection()
        with open(config.SELECT_ALL_EMPLOYEE,"r",encoding="utf-8") as file:
            open_Script = file.read()
        cursor=connection.cursor()
        cursor.execute(open_Script)
        header=[column[0] for column in cursor.description]
        rows=cursor.fetchall()
        return (rows,header)
    except sqlite3.Error as e:
        print("sql error:",e)
        return None, None
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def get_employee_byempid(emp_id):
    connection = None
    cursor = None
    try:
        connection=create_connection()
        cursor=connection.cursor()
        with open(config.SELECT_EMPID_BASED,"r",encoding="utf-8") as file:
            open_script=file.read()
        cursor.execute(open_script,(emp_id,))
        employee=cursor.fetchone()
        return employee
    except sqlite3.Error as e:
        print("sql error:",e)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def update_employee(upd_emp_data,emp_id):
    connection=None
    cursor=None
    try:
        connection=create_connection()
        with open(config.UPDATE_EMP_DATA,"r",encoding="utf-8") as file:
            open_script=file.read()
        cursor=connection.cursor()
        values=(upd_emp_data["First_Name"],
                upd_emp_data["Last_Name"],
                upd_emp_data["Email"],
                upd_emp_data["Phone"],
                upd_emp_data["Department"],
                upd_emp_data["Designation"],
                upd_emp_data["Salary"],
                upd_emp_data["Joining_Date"],
                emp_id)
        cursor.execute(open_script,values)
        connection.commit()
        return("successfully updated")
    except sqlite3.Error as e:
        print("sql error:",e)
        return("update failed")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def delete_employee(empid):
    connection= None
    cursor= None
    try:
        connection=create_connection()
        cursor=connection.cursor()
        with open(config.DELETE_EMP_DATA,"r",encoding="utf-8") as file:
            open_script=file.read()
        cursor.execute(open_script,(empid,))
        rowcount=cursor.rowcount
        connection.commit()
        return rowcount
    except sqlite3.Error as e:
        print("sql error:",e)
        return("error in delete")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()





    
    







