import sparrow
out = sparrow.OutgoingAPI(client_id='client_id',username='username',password='password')
asa=out.sendsms(sender='from',to='to',text_message='message')




