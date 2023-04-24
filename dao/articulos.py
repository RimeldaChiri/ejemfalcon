from dao.conexiondb import mydb
def registrarArticulo(val):
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO articulos(idarticulos, articuloscol) VALUES (%s, %s)", val)
    mydb.commit()

def ListarArticulos(cantidad):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM articulos")
    return mycursor.fetchall(cantidad)
