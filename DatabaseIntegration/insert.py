from connect import *

query = "INSERT INTO customer (NAME, ADDRESS) VALUES (%s, %s)"
val = ("john", "Highway")
val2 = [ ("john", "Highway"),
        ("pandi", "Greams Road"),
        ("sekar", "Thale")
        ]
cursor.execute(query, val)
cursor.executemany(query, val2)

conn.commit()

print(cursor.rowcount, " record inserted")
print("ID : ", cursor.lastrowid)
