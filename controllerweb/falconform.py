import falcon
import dao.articulos

class ThingsResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = 'on_get de thingsResource..........'

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            'metodo post prueba'
        )
class CosasLiz:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_HTML  # Default is JSON, so override
        #resp.cookies.add('nombre1', 'valor1')
        #desde aqui creamos el formulario de la pagina
        resp.text = (
            '<form method="post" action="">'
            '<input type="text" placeholder="Introducir id articulo" name="id" value=""/>'
            '<input type="text" placeholder="Introduce articulo" name="articulo" value=""/>'
            '<input type="submit" value="Enviar dato" />'
            '</form>'
        )  
      
    #ide=13
    def on_post(self, req, resp):   
        #articulo="fosforo"
        #ide=input[1].get('value')
        #articulo=input[2].get('value')
        #self.ide = self.ide + 1
        cantidad = int(req.get_param("cantidad")) or 2
        val = (req.media["id"], req.media["articulo"])      
        dao.articulos.registrarArticulos(val)
        myresult = dao.articulos.ListarArticulos(cantidad)
        var = "{ ["
        for x in myresult:
           var+=f'{{"id":{x[0]},"producto":"{x[1]}"}},'
        resp.text = var+']}'
        #print(dir(req.media))
        resp.media = {
            'params': req.params,
            'media': req.media,
        }
