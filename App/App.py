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
    flag = False

    # Promting the menue, and responding based off the text message
    if body != None:
        response = "\n "
        response = "\nTechieBot\n"
        response += "\nTechieBot - Tech Literacy\n"
        response += "\n1. Setting Up Accounts"
        response += "\n2. Password Management"
        response += "\n3. Managing your Storage"
        response += "\n4. Verifying Emails"
        response += "\n5. Downloading an App"
        response += "\n6. Creating a Reminder"
        response += "\n\nPlease type in the number that corresponds with the option you need help with."
        resp.message(response)
    if body == '1':
        response = "TechieBot\n"
        response += "You chose: Setting Up Accounts\n"
        response += "\n1. If you don't already have the app for the account you're trrying to set up, send a text witgh the number 5.\n"
        response += "\n2. Open the app on your device, and find the signup button.\n"
        response += "\nEnter in your email, and create a password. If you need help with emails send a text with the number 4. Or if you need help with passwords, send the number 2.\n"
        response += "\n3. Answer the following questions. Some common questions include birthdates, usernames, and asking if you would like to receive promo emails. If you don't want to get promo emails, unchek this box.\n"
        response += "\n4. Enjoy your new account!\n"
        resp.message(response)    
    else:
        resp.message("\nI didn't get that.")
    

    return str(resp)
    
if __name__ == "__main__":
    app.run(debug=True)
