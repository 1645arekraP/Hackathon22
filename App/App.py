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
    
    # option 1
    if body == '1':
        response = "TechieBot\n"
        response += "You chose: Setting Up Accounts\n"
        response += "\n1. If you don't already have the app for the account you're trrying to set up, send a text witgh the number 5.\n"
        response += "\n2. Open the app on your device, and find the signup button.\n"
        response += "\nEnter in your email, and create a password. If you need help with emails send a text with the number 4. Or if you need help with passwords, send the number 2.\n"
        response += "\n3. Answer the following questions. Some common questions include birthdates, usernames, and asking if you would like to receive promo emails. If you don't want to get promo emails, unchek this box.\n"
        response += "\n4. Enjoy your new account!\n"
        resp.message(response)

    if body == '2':
        response = "TechieBot\n"
        response += "You chose: Password Managemenet\n"
        response += "\n2a. Resetting a password.\n"
        response += "\n2b. Password Safety.\n"
        resp.message(response)
    if body == '2a':
        response = "1. Visit the webpage you are trying to log in on, and under login click on reset password.\n"
        response += "2. If you're prompted to enter an email, enter the email you've used to register the account.\n"
        response += "3. Continue until you've reached a point where you'll be sent an email.\n"
        response += "4. Check your email, and enter your password.\n"
        resp.message(response)
    if body == '2a':
        response = "- Never use the same passwords for fincancial accounts.\n"
        response += "- If you receive a email asking to reset your password, when you havent gone through the steps yourself, do not reset it through said email! Go to the official webpage, and reset your password from there, this is a common scam called Phishing!\n"
        response += "Don't give passwords out online, and dont keep them in text documents,a good password is a random combination of three words.\n"
        resp.message(response)
    if body == '4':
        response = "TechieBot\n"
        response += "You chose: Verifying Emails\n"
        response += "1. To verify emails, open your email app, and enter the code into what is asking you to verify.\n"
        response += "- Be careful! If you weren't promped that a verification code is being sent, don't enter it!\n"
        response += "- To write an email, click the box titled Compose, and enter the email adress you're trying to send to. Then enter a subject and the content of your email. To attach pictures click on the paper clip in the bottom of the email box, and chose a file to upload.\n"

        resp.message(response)

    elif body != None:
        response = "\nTechieBot\n"
        response += "\nTechieBot - Tech Literacy\n"
        response += "\n1. Setting Up Accounts"
        response += "\n2. Password Management"
        response += "\n3. Managing your Storage"
        response += "\n4. Verifying Emails"
        response += "\n5. Downloading an App"
        response += "\n\nPlease type in the number that corresponds with the option you need help with."
        resp.message(response)    
    

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
