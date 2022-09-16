import os
from twilio.rest import Client
from info import account_sid, auth_token
from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

}

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body != None:
        response = "\n\nTitle Here"
        response += "\n1. Option 1"
        response += "\n2. Option 2"
        response += "\n3. Option 3"
        resp.message(response)
    else:
        resp.message("\nI didnt get that.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
