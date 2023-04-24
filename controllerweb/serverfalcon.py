import falcon
import dao.articulos
#crea la clase ThingResourd, define el metodo on_get y on_pot
class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = 'on_get de thingsResource..........'

    def on_post(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = 'metodo post prueba'
#ide=13
#articulo="fosforo"
class CosasLiz:
    def on_get(self, req, resp):
        """Handles GET requests"""
        #cantidad = int(req.get_param("cantidad")) or 2
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_HTML  # Default is JSON, so override
        #resp.cookies.add('nombre1', 'valor1')
        #desde aqui creamos el formulario de la pagina
        #para leer un archivo
        archivo = open("html/formulario2.html")
        resp.text = archivo.read()
        archivo.close()
        #hasta aqui formulario
    def on_post(self, req, resp):   
        resp.media = {
            'params': req.params,
            'media': req.media,
        }
        #ide=input[1].get('value')
        #articulo=input[2].get('value')
        val = (req.media["id"], req.media["articulo"])      
        dao.articulos.registrarArticulo(val)
        #ide=ide + 1
        #print(dir(req.media))
        #mycursor.execute("SELECT * FROM articulos")

        #myresult = mycursor.fetchall(cantidad)
        
        
        #var = "{ ["
        #for x in myresult:
         #   var+=f'{{"id":{x[0]},"producto":"{x[1]}"}},'
        #resp.text = var+']}'
