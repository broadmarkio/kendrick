'''
Kendrick Engine Implementation

This file contains the implementation of the main thread to be spun when Kendrick is active.
'''

from datetime import datetime

class KendrickEngine(object):
    
    def __init__(self, server_ref, screenshot_ref, urls, s_time, interval):
        
        self.server_ref = server_ref
        self.screenshot_ref = screenshot_ref
        self.urls = urls
        self.s_time = s_time
        self.interval = interval
    
    def capture(self, url):
        
        new_urls = self.screenshot_ref.takeScreenshot(url)
        self.server_ref.update_mapping(new_urls)
    
    def start(self):
        
        while True:
            if datetime.now() >= self.s_time + self.interval:
                self.capture_all()
                self.s_time += self.interval
    
    def capture_all(self):
        
        for url in self.urls:
            self.capture(url)