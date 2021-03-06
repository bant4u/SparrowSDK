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
        self.url = 'http://api.sparrowsms.com/call_in.php?'
        self.client_id = client_id
        self.username = username
        self.password = password
#         values = {'client_id': self.client_id,
#            'username': self.username,
#            'password': self.password,
#            }
#         return self.url_call(values)
      

    
    def sendsms(self,to=None, text_message=None, sender = None):
        values = {'client_id': self.client_id,
                  'username': self.username,
                  'password': self.password,
                  'from': sender,
                  'to': to,
                  'text':text_message
              }
        response_value = self.url_call(values)
        print response_value
        return response_value
        
  
    def url_call(self,values):
        data = urllib.urlencode(values)
        req = urllib2.Request(self.url, data)
        try:
            response = urllib2.urlopen(req)
            response_value = response.read()

        except HTTPError as e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            print "Full error:: ", e.read()


        except URLError as e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason   
            print e.read()
            response_value = e.read() 
        return response_value
        
