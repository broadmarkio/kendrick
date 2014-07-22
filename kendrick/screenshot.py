'''
screenshot.py

This module defines the screenshot class, which is the primary object meant to take screenshots of a page and contact the connections list
to place the screenshot on a webpage.
'''

import sys
import time
from image import Image
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

#Based upon http://stackoverflow.com/questions/1197172/how-can-i-take-a-screenshot-image-of-a-website-using-python

class ScreenShot(object):
    
    def __init__(self):
        
        self.connections_list = []
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)
    
    def takeScreenshot(self, webpage):
        
        self.load(QUrl(webpage.url))
        self.wait_load()
        # set to webpage size
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        # render image
        image_obj = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image_obj)
        frame.render(painter)
        painter.end()
        output_file = 'temp_file.png'
        print 'saving', output_file
        image_obj.save(output_file)
        image_dat = Image(output_file, webpage.title, webpage.url)
        
        connection_urls = []
        
        for conn in self.connections_list:    
            connection_urls.append(conn.changeImage(image_dat))
            
        return connection_urls
    
    def addConnection(self, connection):
        
        self.connections_list.append(connection)
        
    def wait_load(self, delay=0):
        # process app events until page loaded
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True