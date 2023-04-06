#from wsgiref.simple_server import make_server
import falcon
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database = "demo"
)
#print(mydb)
mycursor = mydb.cursor()

 #sql = "INSERT INTO productos (id, producto) VALUES (%s, %s)"
#val = (5, "jabon")
#mycursor.execute(sql, val)
#mydb.commit()

mycursor.execute("SELECT * FROM productos")

myresult = mycursor.fetchall()
#myresult = mycursor.fetchmany(size=2)

#for x in myresult:
  #print(dir(x))
  #print(x[1])



import fibonaci
class Prueba:
    def on_get(self,req,resp):
        cantidad = int(req.get_param("cantidad")) or 2
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM productos")

        myresult = mycursor.fetchmany(cantidad)
        #myresult = mycursor.fetchone()
        #resp.text = myresult

        var = "{ ["
        for x in myresult:
            var+=f'{{"id":{x[0]},"producto":"{x[1]}"}},'
        resp.text = var+']}'    


class Metodo:

    def on_get(self,req,respuesta):
        respuesta.status = falcon.HTTP_200
        respuesta.content_type = falcon.MEDIA_HTML
        r = 4
        if r == 5:
            respuesta.text = (
            '\n <b> Fibonaci de </b>'+str(r)+' es :'+str(fibonaci.fibona(r))
           
            )
        else:
             respuesta.text = (
            '\n <b> Fibonaci de  </b>'+str(r)+' es :'+str(fibonaci.fibona(r))
           
            )    

app = falcon.App()
var = Metodo()
app.add_route('/prac_pagina',var)
app.add_route('/conect_bd',Prueba())
