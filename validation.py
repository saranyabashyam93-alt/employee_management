import database
from datetime import datetime
from datetime import date

def validate_first_name(in_fname):
    char_len=len(in_fname)
    if in_fname == "" :
        return False, "enter first name**"     
    if char_len <= 1:
        return False,"first name should be min 2 char len**"
    if char_len >= 51:
        return False,"first name should be max 50 char len**"
    for char in in_fname:
        if not (char.isalpha() or char==" " or char=="'" or char=="-"):
            return False, "enter only a-z,A-Z,',-,space**"
    return True, in_fname

def validate_last_name(in_lname):    
    char_len=len(in_lname)
    if in_lname == "" :
        return False, "enter last name**"
    if char_len <= 1:
        return False, "last name should be min 2 char len**"
    if char_len >= 51:
        return False,"last name should be max 50 char len**"
    
    for char in in_lname:
        if not (char.isalpha() or char==" " or char=="'" or char=="-"):
            return False, "enter only a-z,A-Z,',-,space**"

    return True, in_lname  

def validate_email(in_emailid):    
    if in_emailid == "":
        return False, "email id missing**"
    if len(in_emailid) >= 251:
        return False, "max of 250 character allowed**"
    if " " in in_emailid:
        return False, "spaces not allowed**"
    if "@" not in in_emailid:
        return False, "@ missing in email id**"
    
    count=in_emailid.count("@")
    if count != 1:
        return False, "only one @ allowed**"
    
    split=in_emailid.split("@")
    if split[0] == "":
        return False, "invalid email id**"
    if split[1] == "":
        return False, "invalid domain**"
    if "." not in split[1]:
        return False, "enter valid email and domain**"
    
    print(f"valid email id: {in_emailid}")
    print("going for duplicate mail id check")
    DB_check =database.DB_email_check(in_emailid)
    if DB_check == True:
        return False, "email id alreday exist**"
    return True,in_emailid

def validate_phonenum(in_phonenum):
    if not in_phonenum.isdigit():
        return False, "enter only digits**"
    if len(in_phonenum) != 10 :
        return False, "phone number should be 10 digits**"
    return True,in_phonenum

def validate_department(in_dept):
    if in_dept == "":
        return False,"missing.please enter department**"
    if not in_dept in ('IT','HR','Finance','Sales','Operations'):
        return False,"should be either IT,HR,Finance,Sales,Operations**"
    return True,in_dept
    
def validate_designation(in_designation):
    length=len(in_designation)
    if in_designation == "":
        return False, "please enter the designation**"
    if not 2 <= length <= 50 :
        return False, "designation should be 2-50 char**"
    return True, in_designation
    
def validate_salary(in_salary):
    in_salary=float(in_salary)
    if in_salary <= 0:
        return False, "salary must be greater than zer0**"
    if in_salary > 1000000:
        return False,"salary should not exceed 1000000**"   
    return True, in_salary       
    
def validate_join_date(in_join_date):
    try:
        if in_join_date == "":
            return False, "date missing**"
        today=date.today()
        join_date=datetime.strptime(in_join_date,"%Y-%m-%d").date()
        join_date_str=datetime.strftime(join_date,"%Y-%m-%d")
        if join_date > today:
            return False, "join date cannot be future date**"
        return True,join_date_str
    except ValueError:
        return False, "invalid date.enter correct joining date**"
    