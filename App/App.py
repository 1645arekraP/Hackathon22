import os
from twilio.rest import Client
from info import account_sid, auth_token
from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Promting the menue, and responding based off the text message
    if body != None:
        response = "\nTechie"
        response += "\nCentral Hub for teaching tech literacy.\nWhat do you need help with?"
        response += "\n1. Setting Up Accounts"
        response += "\n2. Password Management"
        response += "\n3. Managing your Storage"
        response += "\n4. Verifying Emails"
        response += "\n5. Downloading an App"
        response += "\n6. Creating a Reminder"
        resp.message(response)
    else:
        resp.message("\nI didnt get that.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
