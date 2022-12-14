# Hackathon22
# What it does 
-A SMS bot sends a menu whenever a user texts the bot. 
-This menu includes basic digital literacy skills that some people might not have when using technology.
# How we built it 
-We used the Twilio API to send and receive text messages. 
-The Twilio API gets the text from the user and if the body of the SMS text is not a valid choice on the menu, the menu is sent back to the user. 
-The API gets these texts by sending GET and POST requests to a flask environment, and sends texts back to the user by using method. 
# Challenges we ran into 
-The API methods made sub menus behave weirder than we thought. 
-We ended up using basic if/else statements, but in the future, we would like to spend more time with the API to handle these choices better, and to implement more options such as video links. 
-The Flask environment also gave us lots of issues as many of the post and get requests were not throwing errors. 
-To fix this we used a NGROK to tunnel requests from Flask. 
-The app also handles choices as case sensitive strings, a better way to approach this would have been iterating over each character in the string.
# Things to improve
-The Flask environment also gave us lots of issues as many of the post and get requests were not throwing errors. 
-To fix this we used a NGROK to tunnel requests from Flask. The app also handles choices as case sensitive strings, a better way to approach this would have been iterating over each character in the string. 
-Something we wanted to do was also increase the user input, so we also hope to increase more of the user feedback or response, where they are able to ask us more questions and we can answer with more choices. 

# To Do list:
- fix print method (done)
- setup NGROK (High priority)
- fix menu being double printed (High priority)(done)
- check for typos
