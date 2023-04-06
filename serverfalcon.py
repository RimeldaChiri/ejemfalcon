# examples/things.py

# ¡Vamos a empezar esta fiesta!
# PRACTICA DE GITHUB/FORMULARIO/BASE DE DATOS
from wsgiref.simple_server import make_server

import falcon

#desde aqui la conexion a la base de datos
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="baserimelda"
)

mycursor = mydb.cursor()
#hasta aqui la conexion a la base de datos

#para leer un archivo


#fin codigo para leer un archivo


#crea la clase ThingResourd, define el metodo on_get y on_pot
class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            'on_get de thingsResource..........'
        )

    def on_post(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            'metodo post prueba'
        )
#desde aqui creamos el formulario de la pagina
#ide=13
#articulo="fosforo"
class CosasLiz:
    def on_get(self, req, resp):
        """Handles GET requests"""
        #cantidad = int(req.get_param("cantidad")) or 2
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_HTML  # Default is JSON, so override
        #resp.cookies.add('nombre1', 'valor1')
        archivo = open("formulario2.html")
        resp.text = archivo.read()
        archivo.close()
             
    def on_post(self, req, resp):   
        resp.media = {
            'params': req.params,
            'media': req.media,
        }
        #ide=input[1].get('value')
        #articulo=input[2].get('value')
        sql = "INSERT INTO articulos(idarticulos, articuloscol) VALUES (%s, %s)"
        val = (req.media["id"], req.media["articulo"])      
        mycursor.execute(sql,val)
        mydb.commit()
        #ide=ide + 1
        #print(dir(req.media))
        #mycursor.execute("SELECT * FROM articulos")

        #myresult = mycursor.fetchall(cantidad)
        
        
        #var = "{ ["
        #for x in myresult:
         #   var+=f'{{"id":{x[0]},"producto":"{x[1]}"}},'
        #resp.text = var+']}'
            
               
#hasta aqui formulario        
        
# Los recursos están representados por instancias de clase de larga duración.
things = ThingsResource() #creando el objeto things

cosaliz = CosasLiz()

app = falcon.App() 

app.add_route('/rimelda', things)

app.add_route('/formHtml', cosaliz)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()