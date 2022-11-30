from connect import *

query = "DELETE FROM customer WHERE address=%s"
data = ('Highway',)
cursor.execute(query, data)

conn.commit()

print(cursor.rowcount, "record(s) deleted")
