'''
Kendrick Connections File:

This file contains the implementations, as well as the interface, for connections in Kendrick.

--A connection is simply a place to store screenshots once captured within Kendrick. Every connection must adhere to the IConnection
interface in order to perform the following functionality that is expected out of a connection.

=>Give access to a URL that can be accessed with the stored image.
=>Give functionality to allow for creation and deletion of file from external service (or internal if implemented by server)
'''

class IConnection(object):
    
    def __init__(self):
        
        raise NotImplementedError
    
    def getURL(self):
        
        raise NotImplementedError
    
    def addImage(self):
        
        raise NotImplementedError
    
    def removeImage(self):
        
        raise NotImplementedError