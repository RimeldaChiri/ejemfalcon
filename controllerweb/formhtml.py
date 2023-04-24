import falcon
import dao.almacenes

class FormHtml:
    
    def on_get(self,req,resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML
        resp.text = '<b>hola mundo</b>'
        ''' my_cookie_values = req.get_cookie_values('my_cookie')

        resp.set_cookie('my_cookie','valor cookie')

        if my_cookie_values:
            # NOTE: If there are multiple values set for the cookie, you
            #   will need to choose how to handle the additional values.
            var = my_cookie_values[0]
            
        '''


    def on_post(self,req,resp):
        id = int(req.get_param("id"))
        almacen = req.get_param("almacen")
        ubicacion  = req.get_param("ubicacion")
        dao.almacenes.RegistrarAlmacen(id,almacen,ubicacion)

        myresult = dao.almacenes.ListarAll(0,10)
        text = """
            <html> <body>
            <h2>LISTA DE ALMACENES</h2>
            <table border=1>
            <tr>
              <th>ID</th>
              <th>ALMACEN</th>
              <th>UBICACION</th>
            </tr>
            """
        for x in myresult:
            text += "<tr><td>"+str(x[0])+"</td><td>"+x[1]+"</td><td>"+x[2]+"</td></tr>"
        text += "</table></body></html>"

        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML
        resp.text = text
