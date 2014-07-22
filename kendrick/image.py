'''
image.py

This is the image class, which is used to store temporary data for an image, from capturing to pushing it to a connection.
'''

class Image(object):
    
    def __init__(self, path, title, url):
        
        self.path = path
        self.title = title
        self.url = url