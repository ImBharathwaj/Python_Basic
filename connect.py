import psycopg

conn = psycopg.connect("dbname=test user=postgres password=root")
cursor = conn.cursor()

cursor.execute("SELECT * FROM DEPARTMENT_TABLE;")
data = cursor.fetchone()
print("Data fetched from database : ",data)

conn.close()
