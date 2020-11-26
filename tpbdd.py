import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-FHV42EPE\SQLEXPRESS;'
                      'Database=la_gestion_de_personnel;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()
cursor.execute("select * from Module;")
for row in cursor:
    print(row)
    
cursor.execute("INSERT INTO Module VALUES (('machine learning'),('15'),('20'),('10'));")
conn.commit()