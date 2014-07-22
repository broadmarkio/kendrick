'''
Kendrick Server

The kendrick http server is extended from the Tornado project. It serves two purposes

=>To serve static files directly, acts exactly like a connection object.
=>To act as a "proxy" that gives you a particular url to that simply maps to the real url, which is defined
by the connection.
'''

import tornado.ioloop
import tornado.web

class KendrickHandler(tornado.web.RequestHandler):
    
    #Add some shit here...
    pass

class KendrickServer(tornado.web.Application):
    
    def __init__(self, handler_array):
        
        super.__init__(handler_array)