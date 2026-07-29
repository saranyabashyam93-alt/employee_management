CREATE TABLE IF NOT EXISTS EMPLOYEES
            (Employee_ID INTEGER PRIMARY KEY AUTOINCREMENT,
             First_Name TEXT NOT NULL,
             Last_Name TEXT NOT NULL,
             Email TEXT NOT NULL UNIQUE,
             Phone TEXT NOT NULL,
             Department TEXT NOT NULL CHECK 
             (department IN 
              ( 'IT',
                'HR',
                'Finance',
                'Sales',
                'Operations')),
             Designation TEXT NOT NULL,
             Salary REAL NOT NULL CHECK (salary > 0),
             Joining_Date TEXT NOT NULL);