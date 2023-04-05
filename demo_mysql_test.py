import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="baserimelda"
)

#print(mydb)
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("CREATE DATABASE baseRimelda")

#mycursor.execute("SHOW DATABASES") muestra las bases de datos creados

#for x in mycursor:
 # print(x)
 
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = [
  #('Peter', 'Lowstreet 4'),
  #('Amy', 'Apple st 652'),
  #('Hannah', 'Mountain 21'),
  #('Michael', 'Valley 345'),
  #('Sandy', 'Ocean blvd 2'),
  #('Betty', 'Green Grass 1'),
  #('Richard', 'Sky st 331'),
  #('Susan', 'One way 98'),
  #('Vicky', 'Yellow Garden 2'),
  #('Ben', 'Park Lane 38'),
  #('William', 'Central st 954'),
  #('Chuck', 'Main Road 989'),
 # ('Viola', 'Sideway 1633')
#]

sql = "INSERT INTO articulos (idarticulos, articuloscol) VALUES (%s, %s)"
val = [
  ('5', 'brohes')
 ]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "datos insertados")