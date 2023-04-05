import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="baserimelda"
)

mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM customers")
mycursor.execute("SELECT * FROM articulos")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)