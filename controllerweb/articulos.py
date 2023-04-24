import falcon
import json
import dao.articulos

class InsertatArticulos(object):
    def on_get(self, req, res):
        val = [
                ('5', 'Broches'),
                ('6', 'Evillas')
        ]
        numeroInsertados = dao.articulos.registrarMuchosArticulos(val)
        res.status = falcon.HTTP_200
        res.content_type = falcon.MEDIA_JSON
        res.text = json.dumps({'numeroInsertados': numeroInsertados
                               , 'nombre': 'articulos'})
