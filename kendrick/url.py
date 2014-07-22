'''
Kendrick url.py

Defines the url class, which is the primary unit of association of a webpage to be stored. Each webpage has a persistent url that receives a request
and proxies the request to a particular connection.
'''

class Url(object):
    
    def __init__(self, url):
        
        self.url = url
    
    def getUrl(self):
        
        pass