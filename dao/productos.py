from dao.conexiondb import mydb

def registrarProducto(id, nombre):
    mycursor = mydb.cursor()
    #val = (5, "jabon")
    mycursor.execute(
        "INSERT INTO productos (id, producto) VALUES (%s, %s)"
        , (id, nombre))
    mydb.commit()

def ListarPrductos():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM productos")
    myresult = mycursor.fetchall()
    #myresult = mycursor.fetchmany(size=2)
    #for x in myresult:
        #print(dir(x))
        #print(x[1])
    return myresult

def ListarPrductosCantidad(cantidad):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM productos")
    return mycursor.fetchmany(cantidad)
    #return mycursor.fetchone()
