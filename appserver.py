from wsgiref.simple_server import make_server
import falcon
from controllerweb.Almacenes import ListaAlmacenes
from controllerweb.formhtml import FormHtml
from controllerweb.falconform import CosasLiz
from controllerweb.falconform import ThingsResource
import controllerweb.serverfalcon
import controllerweb.prac_pagina

listAlmacenes = ListaAlmacenes()
app = falcon.App()
# Los recursos están representados por instancias de clase de larga duración.
app.add_route('/json', listAlmacenes)
app.add_route('/almacenes/insert', FormHtml())
#app.add_route('/conexion',Conexion())
app.add_route('/rimelda', ThingsResource())#creando el objeto things, ademas lo asociamos a la URL '/rimelda'
app.add_route('/formHtml', CosasLiz())
app.add_route('/rimelda2', controllerweb.serverfalcon.ThingsResource())
app.add_route('/formHtml2', controllerweb.serverfalcon.CosasLiz())
app.add_route('/metodo', controllerweb.prac_pagina.Metodo())
app.add_route('/prueba', controllerweb.prac_pagina.Prueba())

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
#waitress-serve --port=8000 appserver:app

#https://www.oracle.com/database/technologies/appdev/python/quickstartpythononprem.html
#https://python-oracledb.readthedocs.io/en/latest/user_guide/installation.html#installing-python-oracledb-on-windows
#https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html#ic_winx64_inst
#https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170
#https://www.oracle.com/database/technologies/appdev/xe.html
#https://python-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html
#https://docs.public.oneportal.content.oci.oraclecloud.com/en-us/iaas/autonomous-database-shared/doc/connecting-python-tls.html
#https://stackoverflow.com/questions/72400478/with-python-oracledb-what-does-dpy-4027-no-configuration-directory-to-search-f
