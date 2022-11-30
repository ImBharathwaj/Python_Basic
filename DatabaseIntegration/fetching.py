from connect import *

query = "SELECT * FROM customer ORDER BY ADDRESS"
cursor.execute(query)

# To fetch single result
my_result = cursor.fetchone()

# To fetch all result from query
my_result = cursor.fetchall()

for _ in my_result:
    print(_)
