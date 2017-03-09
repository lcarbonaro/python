import sqlite3

with sqlite3.connect("meetup.db") as connection:
    conn = connection.cursor()
    
    more_emps = [
            ("Kenneth", "Boole", "Marketer"),
            ("Sean", "Connery", "Actor"),
            ("Justin", "Trudeau", "Prime Minister")
        ]
        
    conn.executemany("INSERT INTO employees VALUES(?, ?, ?)", more_emps)
    conn.execute("UPDATE employees SET job_title = 'Director' WHERE firstname = 'Sean'")
    conn.execute("SELECT * FROM employees")
    emp_data = conn.fetchall()
    for emp in emp_data:
        print("Employees:{0} {1} {2}".format(emp[0], emp[1], emp[2]))