import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = '',
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE Database")

print("database berhasil dibuat")
