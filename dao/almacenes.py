from dao.conexiondb import mydb

def EliminarAlmacen(id):
        sql = "DELETE FROM ALMACENES WHERE ID ="+str(id)
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()

def RegistrarAlmacen(id,almacen,ubicacion):
        sql = "INSERT  INTO ALMACENES(ID,ALMACEN,UBICACION) VALUES (%s,%s,%s)"
        val = (id,almacen,ubicacion)
        mycursor = mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit() 

def ModificarAlmacen(id,almacen,ubicacion):    
        sql = "UPDATE  ALMACENES SET ALMACEN=%s,UBICACION=%s WHERE ID="+str(id)
        val = (almacen,ubicacion)
        mycursor = mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit() 

def ListarAll(offset, limit):
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM ALMACENES limit {limit} offset {offset}")
        # mycursor.execute(f"select id, name, description, fechaalta from role order by id OFFSET {inicio} ROWS FETCH NEXT {limit} ROWS ONLY")
        return mycursor.fetchall()
