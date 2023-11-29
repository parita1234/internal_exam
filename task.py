import mysql.connector
mydb = mysql.connector.connect(
  host="",
  user="admin",
  password="",
 
)

mycursor = mydb.cursor()

mycursor.execute("SHOW databases")

for x in mycursor:
     print(x)