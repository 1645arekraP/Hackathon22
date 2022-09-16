# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC7137af2650c535a1925bddf0bb279242'
auth_token = '4b2af6af03e97da3e261a07a1b3ec97e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17573491472',
                     to='+17703127914'
                 )

print(message.sid)