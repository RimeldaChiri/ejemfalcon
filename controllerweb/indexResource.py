import falcon
import json
from mysql.conexiondb import mycursor

class ListaAlmacenes(object):
  def on_get(self, req, res):
    res.status = falcon.HTTP_200
    res.content_type = falcon.MEDIA_JSON
    limit = int(req.get_param("limit"))
    inicio = int(req.get_param("inicio"))
    
    mycursor.execute(f"SELECT * FROM ALMACENES limit {limit} offset {inicio}")
    myresult = {'data':mycursor.fetchall(),'nombre':'almacenes'}
    res.body = json.dumps(myresult)