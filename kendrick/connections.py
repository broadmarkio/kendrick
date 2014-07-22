'''
Kendrick Connections File:

This file contains the implementations, as well as the interface, for connections in Kendrick.

--A connection is simply a place to store screenshots once captured within Kendrick. Every connection must adhere to the IConnection
interface in order to perform the following functionality that is expected out of a connection.

=>Give access to a URL that can be accessed with the stored image.
=>Give functionality to allow for creation and deletion of file from external service (or internal if implemented by server)
'''

import pyimgur

class IConnection(object):
    
    def __init__(self):
        
        raise NotImplementedError
    
    def getURL(self):
        
        raise NotImplementedError
    
    def changeImage(self):
        
        raise NotImplementedError
    
    
class ImgurConnection(IConnection):
    
    def __init__(self, api_key):
        
        self.api_key = api_key
        
        #Map Web-address to imgur url
        self.url_mapping = {}
    
    def getURL(self, webpage):
        
        return self.url_mapping[webpage.url]
    
    def changeImage(self, image):
        
        imgur = pyimgur.Imgur(self.api_key)
        uploaded_img = imgur.upload_image(image.path, title=image.title)
        self.url_mapping[image.url] = uploaded_img.link
        return uploaded_img.link