#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.
from twilio.rest import TwilioRestClient

# Preset values:
accountSID = 'ACc5ce8b19ff7c50663c5ba5427fc824ec'
authToken  = '4abb7392c8a43b6c152a39d7a876eb8b'
myNumber = '+17573383781'
twilioNumber = '+12529220012'


def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
