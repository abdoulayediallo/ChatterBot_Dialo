#######################
#IMPORT PACKAGE
#######################

#Retrieval-based models 
from chatterbot import ChatBot

#Web application
from flask import Flask, render_template, request, jsonify  

#Forms
from wtforms import Form, TextAreaField, validators 

#Artificial intelligence markup language. AIML is a form of XML that defines rules for matching patterns and determining responses.
import aiml

#importing file from aiml
import os   


#########################################
# Create a new chat bot named Muta
#########################################
#information here http://chatterbot.readthedocs.io/en/stable/tutorial.html

mychatbot = ChatBot(
            "Muta", 
            read_only=False,  #To disable the learning feature after your bot has been trained, set read_only=True
            storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",     #simple storage adapter that stores data in a json formatted file on your hard disk.
            database="mydatabase.json",
            logic_adapters=[
                            "chatterbot.adapters.logic.MathematicalEvaluation", #TimeLogicAdapter
                            "chatterbot.adapters.logic.TimeLogicAdapter", #  solves math problems 
                            "chatterbot.adapters.logic.ClosestMatchAdapter",
                            "chatterbot.adapters.logic.ClosestMeaningAdapter"
            ],
            input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",  #reads the user input from python
            output_adapter="chatterbot.adapters.output.OutputFormatAdapter" #return a response in Json
        )
        

    


###########################################
# TRAIN THE BOT
###########################################
#The current training method takes a list of statements that represent a conversation

# Train based on the english corpus
from chatterbot.trainers import ListTrainer

#Training via list data
#........................
#http://chatterbot.readthedocs.io/en/stable/training.html#training-with-corpus-data

mychatbot.set_trainer(ListTrainer)

mychatbot.train([
    "Salut",
    "Bonjour",
])

mychatbot.train([
    "Hello",
    "Bonjour",
])

mychatbot.train([
    "Bonjour",
    "Bonjour",
])

mychatbot.train([
    "Bonjour",
    "Comment allez-vous",
    "Tres bien merci",
    "Heureux de l entendre",
    "Merci",
    "Avec plaisir"
])



#Training with corpus data
#.............................
# http://chatterbot.readthedocs.io/en/stable/training.html#training-with-corpus-data

from chatterbot.trainers import ChatterBotCorpusTrainer

mychatbot.set_trainer(ChatterBotCorpusTrainer)
mychatbot.train(
    "chatterbot.corpus.french.greetings", "chatterbot.corpus.french.trivia"
)




###################################
#CREATE THE APP
##################################

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
	
	#By specifying a session, the AIML can tailor different conversations to different people.
	#This is good for having personalized conversations with each client
	#To specify which session you are using you pass it as a second parameter to respond().
	# (ref. http://www.devdungeon.com/content/ai-chat-bot-python-aiml)
	sessionID = 12345
	while True:
	    if message == "quit":
	        exit()
	    else:
	        bot_response = str(mychatbot.get_response(message))
	        # print bot_response
	        return jsonify({'status':'OK','answer':bot_response})
    
    # Get session info as dictionary. Contains the input
    # and output history as well as any predicates known
    #sessionData = kernel.getSessionData(sessionID)

if __name__ == '__main__':
    app.run(debug=True)     #lance application en mode debug. Attention, a supprimer quand le site sera disponible sur internet









