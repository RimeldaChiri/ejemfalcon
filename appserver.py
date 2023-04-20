import falcon
from controllerweb.indexResource import ListaAlmacenes

app = falcon.App()
app.add_route('/json',ListaAlmacenes())
#app.add_route('/conexion',Conexion())

#waitress-serve --port=8000 appserver:app