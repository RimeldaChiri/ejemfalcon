import falcon
import json
import dao.almacenes

class ListaAlmacenes(object):
    def on_get(self, req, res):
        limit = int(req.get_param("limit"))
        inicio = int(req.get_param("inicio"))

        res.status = falcon.HTTP_200
        res.content_type = falcon.MEDIA_JSON
        res.text = json.dumps({'data': dao.almacenes.ListarAll(inicio, limit), 'nombre': 'almacenes'})
