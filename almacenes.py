#class almacenes:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database = "demo"
  )

mycursor = mydb.cursor()
def EliminarAlmacen(id):
        sql = "DELETE FROM ALMACENES WHERE ID ="+str(id)
        mycursor.execute(sql)
        mydb.commit()

def RegistrarAlmacen(id,almacen,ubicacion):
        sql = "INSERT  INTO ALMACENES(ID,ALMACEN,UBICACION) VALUES (%s,%s,%s)"
        val = (id,almacen,ubicacion)
        mycursor.execute(sql,val)
        mydb.commit() 
def ModificarAlmacen(id,nombres,ci):    
        sql = "UPDATE  ALMACENES SET ALMACEN=%s,UBICACION=%s WHERE ID="+str(id)
        val = (almacen,ubicacion)
        mycursor.execute(sql,val)
        mydb.commit() 

