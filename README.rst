

Facebook Python SDK

This client library is designed to support the Sparrow sms Api and the official SparrowSmsSDK, which is the canonical way to implement Sparrow sms Outgoing api. You can read more about the API by accessing its official documentation.

Basic usage:
*******************************

import sparrow
out = sparrow.OutgoingAPI('client_id','username','password','url')
out.sendsms('from','to','message')

*******************************
Having trouble with Pages? we’ll help you sort it out.

