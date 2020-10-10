
from werkzeug.wrappers import Request, Response, ResponseStream

class middleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        let auth = request.headers.Authorization
        let token = auth.split(" ")
       
        if token[0] != "Bearer":
            res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        if
        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
        

        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)
