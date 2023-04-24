import falcon
import controllerweb.fibonaci as fibonaci
import dao.productos

class Prueba:
    def on_get(self,req,resp):
        cantidad = int(req.get_param("cantidad")) or 2
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        myresult = dao.productos.ListarPrductosCantidad(cantidad)
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
            respuesta.text = '\n <b> Fibonaci de </b>'+str(r)+' es :'+str(fibonaci.fibona(r))
        else:
            respuesta.text = '\n <b> Fibonaci de </b>'+str(r)+' es :'+str(fibonaci.fibona(r))
