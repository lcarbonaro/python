import sqlite3

connection = sqlite3.connect("meetup.db")
conn = connection.cursor()
conn.execute("CREATE TABLE IF NOT EXISTS employees(firstname TEXT, lastname TEXT, job_title TEXT)")
conn.execute("INSERT INTO employees VALUES('James', 'Brown', 'Designer')")

emps = [
        ("Henry", "Ford", "Engineer"),
        ("David", "Blaine", "Illusionist"),
        ("Martha", "Scott", "Doctor"),
        ("Mike", "Malloney", "Architect")
    ]
conn.executemany("INSERT INTO employees VALUES(?, ?, ?)", emps)
connection.commit()
conn.execute("SELECT * FROM employees")
emp = conn.fetchall()
for e in emp:
    print(e)

connection.close()

