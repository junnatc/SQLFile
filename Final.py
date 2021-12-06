import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="213712656",
    database="menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM  pet")
for x in mycursor:
    print(x)
print(mydb)
