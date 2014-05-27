'''
Created on May 26, 2014

@author: bijay
'''
import unittest
from sparrow import OutgoingAPI


class Test(unittest.TestCase):

    def setUp(self,):
        self.client_id = 'bijay'
        self.username = 'bijay'
        self.password = 'bijay'
        self.url = None

    def tearDown(self):
        print "Success"

    def test_outgoing_with_username_only(self):
        out = OutgoingAPI("",'bijay',"",None)
        resp = out.sendsms('9848848484', '9848848484', 'Hello world')
        self.assertIn('Error 1: 403 - You must be someone', resp)
    
    def test_outgoing_with_client_id_only(self):
        out = OutgoingAPI("bijay","","",None)
        resp = out.sendsms('9848848484', '9848848484', 'Hello world')
        self.assertIn('Error 1.1: 403 - Username', resp)
    
    def test_outgoing_with_password_only(self):
        out = OutgoingAPI("","","bijay",None)
        resp = out.sendsms('9848848484', '9848848484', 'Hello world')
        self.assertIn("Error 1.1: 403 - Username isn't supplied", resp)
    
    # testing the Api if no client_id is supplied
    def test_outgoing_without_client(self):
        out = OutgoingAPI('','bijay','bijay',None) 
        resp = out.sendsms('9848442934', '9845454545','Hello')
        self.assertIn("Error 1: 403 - You must",resp)
    
    # testing the Api if no password is supplied
    def test_outgoing_without_password(self):
        out = OutgoingAPI('bijay','bijay','',None) 
        resp = out.sendsms('9848442934', '9845454545','Hello')
        self.assertIn("Error 2: 403 - Unauthorized",resp)
    
    def test_outgoing_without_username(self):
        out = OutgoingAPI('bijay',None,'bijay',None) 
        resp = out.sendsms('9848442934', '9845454545','Hello')
        self.assertIn("Error 2: 403",resp)
    
    def test_sendsms_without_from(self):
        out = OutgoingAPI('bijay','bijay','bijay',None) 
        resp = out.sendsms('9848442934', '','Hello')
        print resp
        #self.assertIn("",resp)
    
    def test_sendsms_without_to(self):
        out = OutgoingAPI('bijay','bijay','bijay',None) 
        resp = out.sendsms('9848442934', '','Hello')
        #self.assertIn("",resp)
        print resp
    
    
    def test_sendsms_without_message(self):
        out = OutgoingAPI('bijay','bijay','bijay',None) 
        resp = out.sendsms('9848442934','9834343434','')
        #self.assertIn("",resp)
        print resp

    
    def test_sendsms_(self):
        out = OutgoingAPI('bijay','bijay','bijay',None)
        resp = out.sendsms('9848442934','9834343434','Hello')
        print resp

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()