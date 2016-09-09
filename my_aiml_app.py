#! /usr/bin/python
# -*- coding:utf-8 -*-

#Import Package
from flask import Flask, render_template, request, jsonify   #Web application
from wtforms import Form, TextAreaField, validators          #Forms
import aiml  #Artificial intelligence markup language. AIML is a form of XML that defines rules for matching patterns and determining responses.
import os   #importing file from aiml
    

#Initialized a new flask instance
app = Flask(__name__) 
app.secret_key = 'quelquechosedecompliqueratrouver'


#Render the homepage
@app.route('/')
def main():
    return render_template('index.html')
    
#Load the bot brain (or if not existing read ailm files)  + Answer questions
@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])

    # The Kernel object is the public interface to
    # the AIML interpreter.
	kernel = aiml.Kernel()

    #When you start to have a lot of AIML files, it can take a long time to learn. 
    #This is where brain files come in. 
    #After the bot learns all the AIML files it can save its brain directly to a file which will drastically speed up load times on subsequent runs.
	# (ref. http://www.devdungeon.com/content/ai-chat-bot-python-aiml)
	if os.path.isfile("bot_brain.brn"):  
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml_corpus/std-startup.xml"), commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")

	# kernel now ready for use
	#By specifying a session, the AIML can tailor different conversations to different people.
	#This is good for having personalized conversations with each client
	#To specify which session you are using you pass it as a second parameter to respond().
	# (ref. http://www.devdungeon.com/content/ai-chat-bot-python-aiml)
	sessionID = 12345
	while True:
	    if message == "quit":
	        exit()
	    elif message == "save":
	        kernel.saveBrain("bot_brain.brn")
	    else:
	        bot_response = kernel.respond(message, sessionID)
	        # print bot_response
	        return jsonify({'status':'OK','answer':bot_response})
    
    # Get session info as dictionary. Contains the input
    # and output history as well as any predicates known
    #sessionData = kernel.getSessionData(sessionID)

    
@app.route('/contact/')
def contact():
    mail = "sven.wauters@mc.be"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


if __name__ == '__main__':
    app.run(debug=True)     #lance l'app en mode debug. Attention, à supprimer quand le site sera disponible sur internet!
