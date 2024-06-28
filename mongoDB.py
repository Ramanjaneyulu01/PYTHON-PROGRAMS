import mysql.connector

mydb = mysql.connector.connect(host="localhost",    user="root", password="Pradeep123#",   database="mydb")

mycurs = mydb.cursor()
mycurs.execute("CREATE TABLE users (name VARCHAR(50), email VARCHAR(50), password VARCHAR(50))")
mycurs.execute("SHOW TABLES")
mycurs.execute("Insert Int(")

for table in mycurs:
    print(table)
