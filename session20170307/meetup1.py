import sqlite3
import csv

with sqlite3.connect("meetup.db") as connection:
    conn = connection.cursor()
    conn.execute("CREATE TABLE IF NOT EXISTS employees2(firstname TEXT, lastname TEXT, gender TEXT)")
    
    employee_file = csv.reader(open("employees.csv", "rU"))
    employee_file.next()
    
    conn.executemany("INSERT INTO employees2 VALUES(?, ?, ?)", employee_file)
    conn.execute("SELECT * FROM employees2")
    csv_emps_data = conn.fetchall()
    
    for emp in csv_emps_data:
        print("Employees: {0} {1} {2}".format(emp[0], emp[1], emp[2]))