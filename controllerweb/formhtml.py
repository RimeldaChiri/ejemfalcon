import falcon
from mysql.conexiondb import mycursor
from almacenes import almacenes
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