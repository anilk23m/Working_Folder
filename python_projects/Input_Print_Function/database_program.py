import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=(localdb)\MSSQLLocalDb;"
    "DATABASE=EmployeesDb;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
cursor.execute("select * from Employees")
data = cursor.fetchall()

print(data)

