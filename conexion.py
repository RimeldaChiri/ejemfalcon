import falcon
import mysql.connector
import almacenes
import json
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database = "demo"
  )

mycursor = mydb.cursor()
#waitress-serve --port=8000 conexion:app
class IndexResource(object):
  def on_get(self, req, res):
    res.status = falcon.HTTP_200
    res.content_type = falcon.MEDIA_JSON
    limit = int(req.get_param("limit"))
    inicio = int(req.get_param("inicio"))
    
    mycursor.execute(f"SELECT * FROM ALMACENES limit {limit} offset {inicio}")
    myresult = {'data':mycursor.fetchall(),'nombre':'almacenes'}
    res.body = json.dumps(myresult)


class Conexion:
    
    def on_post(self,req,resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML
        resp.text = (
            '   <b>   hola </b>'
            )
        
        ''' my_cookie_values = req.get_cookie_values('my_cookie')
        
        resp.set_cookie('my_cookie','valor cookie')

        if my_cookie_values:
            # NOTE: If there are multiple values set for the cookie, you
            #   will need to choose how to handle the additional values.
            var = my_cookie_values[0]
            
        '''
    
    def on_get(self,req,resp):
        
        #resp.set_cookie('my_cookie','valor cookie')

        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML
        id = int(req.get_param("id"))
        almacen = req.get_param("almacen")
        ubicacion  = req.get_param("ubicacion")
        almacenes.RegistrarAlmacen(id,almacen,ubicacion)
        mycursor.execute("SELECT * FROM ALMACENES")
        myresult = mycursor.fetchall()

        # var = ' '
        #for x in myresult:
         #  var+=" ID:"+str(x[0])+" ALMACEN:"+x[1]+" UBICACION:"+x[2]
          
        #resp.text = var
        resp.text =(
            '<html> <body> '
            '<h2>LISTA DE ALMACENES</h2>'
            '<table border=1>'
            '<tr>'
              '<th>ID</th>'
              '<th>ALMACEN</th>'
              '<th>UBICACION</th>'
            '</tr>'
            '</table>'
            '</body></html>'
        )
        
       
        #resp.text = (myresult) 
class FormHtml:
    
    def on_post(self,req,resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML
        resp.text = (
            '   <b>   hola </b>'
            )
        
        
    
    def on_get(self,req,resp):
        
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML
        id = int(req.get_param("id"))
        almacen = req.get_param("almacen")
        ubicacion  = req.get_param("ubicacion")
        almacenes.RegistrarAlmacen(id,almacen,ubicacion)
        mycursor.execute("SELECT * FROM ALMACENES")
        myresult = mycursor.fetchall()

        # var = ' '
        #for x in myresult:
         #  var+=" ID:"+str(x[0])+" ALMACEN:"+x[1]+" UBICACION:"+x[2]
          
        #resp.text = var
        resp.text =(
            '<html> <body> '
            '<h2>LISTA DE ALMACENES</h2>'
            '<table border=1>'
            '<tr>'
              '<th>ID</th>'
              '<th>ALMACEN</th>'
              '<th>UBICACION</th>'
            '</tr>'
            '</table>'
            '</body></html>'
        )
        
       
        #resp.text = (myresult)        
  
app = falcon.App()
#almacenes.RegistrarAlmacen(2,"almacen 2","las panosas")
almacenes.EliminarAlmacen(34)

app.add_route('/json',IndexResource())
app.add_route('/conexion',Conexion())