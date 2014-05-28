#!/usr/bin/env python
# encoding: utf-8
'''
sparrow.send -- shortdesc

sparrow.send is a description

It defines classes_and_methods

@author:     bijaypant1@gmail.com

@copyright:  2014 Janaki Technology. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

from optparse import OptionParser
import sparrow

def main():
    usage = "useage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-c","--clientid", type="string", dest="client_id",default=None, help="Ex.CLIENT_ID")
    parser.add_option("--username", type="string", dest="username",default=None,help="Username Ex. bijay")
    parser.add_option("--password",type="string",dest="password",default=None,help="Refer vault password for security")
    parser.add_option("--sender",type="string", dest="sender",default=None, help="Ex. true or false")
    parser.add_option("--to", type="string", dest="to",default=None, help="Ex. Yes or No")
    parser.add_option("--text", type="string", dest="text_message",default=None, help="Ex. Yes or No")
    (options, args) = parser.parse_args()

    if options.client_id is None:
        print "Client ID is not supplied and is Requird "
    if options.username is None:
        print "Username is not supplied  and is Required"
    if options.password is None:
        print "Password is not supplied and is Required"
    if options.to is None:
        print "TO location is not supplied and is Required "
    if options.text_message is None:
        print "Text Message is not Provided, You would like to do so. "
    if options.sender is None:
        print "You choose to use default sender address "
            
    if options.client_id and options.username and options.password and options.to and options.text_message:
        out = sparrow.OutgoingAPI(client_id = options.client_id,username = options.username, password = options.password)
        print out.sendsms(to=options.to, text_message = options.text_message, sender=options.sender)
        
if __name__ == "__main__":
    main()