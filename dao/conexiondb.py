import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database = "baserimelda"
  )

#mycursor = mydb.cursor()
#for x in mycursor:
 # print(x)

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("CREATE DATABASE baseRimelda")

#mycursor.execute("SHOW DATABASES") muestra las bases de datos creados
