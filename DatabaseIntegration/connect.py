import mysql.connector as connector

conn = connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='test'
        )

cursor = conn.cursor()
