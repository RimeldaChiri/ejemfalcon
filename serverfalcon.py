# examples/things.py

# ¡Vamos a empezar esta fiesta!
from wsgiref.simple_server import make_server

import falcon


# Falcon sigue el estilo arquitectónico REST, lo que significa (entre
# otras cosas) que piensas en términos de recursos y transiciones de estado,
# que se asignan a verbos HTTP.
class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            'on_get de thingsResource..........'
        )

    def on_post(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            'metodo post prueba'
        )
class CosasLiz:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_HTML  # Default is JSON, so override
        #resp.cookies.add('nombre1', 'valor1')
        resp.text = (
            '<b>cosas de liz</b>'
        )       

# Los recursos están representados por instancias de clase de larga duración.
things = ThingsResource() #creando el objeto things

cosaliz = CosasLiz()

app = falcon.App() 

app.add_route('/rimelda', things)

app.add_route('/cosasliz', cosaliz)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()