# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from info import account_sid, auth_token


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17573491472',
                     to='+17703127914'
                 )

print(message.sid)
