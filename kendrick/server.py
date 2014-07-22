'''
Kendrick Server

The kendrick http server is extended from the Tornado project. It serves two purposes

=>To serve static files directly, acts exactly like a connection object.
=>To act as a "proxy" that gives you a particular url to that simply maps to the real url, which is defined
by the connection.
'''

import tornado.ioloop
import tornado.web
import threading

server_lock = threading.Lock()

class ImageProxyHandler(tornado.web.RequestHandler):
    
    def get(self):
        
        connection = self.get_argument("c")
        title = self.get_argument("t")
        
        self.write(chunk)
        
        with server_lock:
            

class KendrickServer(tornado.web.Application):
    
    def __init__(self):
        
        self.mapping = {}
        
        super.__init__([
                        (r"/image", ImageProxyHandler)
                        ])
        
    def addToMapping(self, webpage):
        
        self.mapping[webpage.title] = 0
            
    def removeFromMapping(self, webpage):
        
        del self.mapping[webpage.title]
    
    def updateMapping(self, webpage, urls):
        
        with server_lock:
            self.mapping[webpage.title] = urls
            
    def start(self):
        
        pass