'''
Created on May 26, 2014

@author: bijay
'''
#!/usr/bin/env python

import urllib
import urllib2
from urllib2 import HTTPError,URLError
import requests
import json

class OutgoingAPI():
    
    def __init__(self,client_id=None, username=None, password=None,url= None,):
        if url == None:
            self.url = 'http://api.sparrowsms.com/call_in.php?'
        else:
            self.url=url
        self.client_id = client_id
        self.username = username
        print self.url
    
    def sendsms(self, sender, to , text_message):
        values = {'client_id': self.client_id,
          'username': self.username,
          'password': self.password,
          'from': sender,
          'to': to,
          'text':text_message
          }
        data = urllib.urlencode(values)
        req = urllib2.Request(self.url, data)
        try:
            response = urllib2.urlopen(req)
            response_value = response.read()
            print response_value
        except HTTPError as e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            print e.read()

        except URLError as e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        
