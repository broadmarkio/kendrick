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
import urllib
from lib.rwlock import RWLock
from requests.packages import urllib3

server_lock = RWLock()
mapping = {}

class ImageProxyHandler(tornado.web.RequestHandler):
    
    def get(self):
        
        connection = self.get_argument("c")
        title = self.get_argument("t")
        
        server_lock.reader_acquire()
        dat_arr = mapping[title]
        server_lock.reader_release()
        
        html_file = urllib.urlopen(dat_arr[connection])
        self.write(html_file)
        self.flush()
            
class KendrickServer(tornado.web.Application):
    
    def __init__(self):
        
        super.__init__([
                        (r"/image", ImageProxyHandler)
                        ])
        
    def addToMapping(self, webpage):
        
        mapping[webpage.title] = 0
            
    def removeFromMapping(self, webpage):
        
        del mapping[webpage.title]
    
    def updateMapping(self, webpage, urls):
        
        server_lock.writer_acquire()
        mapping[webpage.title] = urls
        server_lock.writer_release()
            
    def start(self):
        self.listen(8888)
        tornado.ioloop.IOLoop.instance().start()