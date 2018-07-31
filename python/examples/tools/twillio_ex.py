from twilio.rest import TwilioRestClient

account_sid = 'ACc5ce8b19ff7c50663c5ba5427fc824ec'
auth_token = '4abb7392c8a43b6c152a39d7a876eb8b'
twilio_cli = TwilioRestClient(account_sid, auth_token)
my_twilio_number = '+12529220012'
my_cell_phone = '+17573383781'
message = twilio_cli.messages.create(body='Mr. Watson - Come here - I want to see you.',
                                     from_=my_twilio_number, to=my_cell_phone)

message.to
message.from_
message.body
message.status
message.date_created
datetime.datetime(2015, 7, 8, 1, 36, 18)
message.date_sent == None
message.sid
updatedMessage = twilioCli.messages.get(message.sid)
updatedMessage.status
updatedMessage.date_sent