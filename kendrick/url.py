'''
Kendrick url.py

Defines the url class, which is the primary unit of association of a webpage to be stored. Each webpage has a persistent url that receives a request
and proxies the request to a particular connection.
'''

class Url(object):
    
    def __init__(self, url, title):
        
        self.url = url
        self.title = title
    
    def getUrl(self):
        
        return self.url
    
class UrlsCollection(object):
    
    def __init__(self):
        
        self.store = {}
        
    def addUrl(self, url_obj):
        
        self.store[url_obj.title] = url_obj
        
    def removeUrl(self, title):
        
        del self.store[title]
        
    def get_collection(self):
        
        return self.store.values()