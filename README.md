# ChatterBot_Dialo

Ce n'est probablement pas très claire. N'hésites pas à m'appeler pour plus d'explication... Tu auras quelque chose de mieux la semaine prochaine :-)s

## LANCER L'APP

Tu vas en ligne de commande dans le fichier
- tu installes les libraries (chatterbot et autres) avec pip install chatterbot
- tu lances l'application avec python my_aiml_app.py

Ce n'est probablement pas très claire. N'hésites pas à m'appeler pour plus d'explication... Tu auras quelque chose de mieux la semaine prochaine :-)s


## Explication des fichiers

### My_.._APP.py  (ie my_AIML_app & my chatterbot_app)
C'est les coeur de l'application. C'est lui qui fait fait tout le backend. My_AIML_APP est une application qui utilise la library AIML du projet ALICE et my_CHATTERBOT et une autre application qui est basée sur la library CHATTERBOT en pure Python. Perso, j'aurais tendence à abandonner AIML pour Chatterbot pour avec full control et flexibilité. 

### CORPUS (AIML and CHATTERBOT)
Ce sont les textes contenant les conversations qui servent de training au robot. Le corpus AIML vient du projet open source ALICE. Apparemment assez populaire dans les année 2004. Le corpus Chatterbot vient de la library python CHATTERBOT dont je t'ai déjà parlé. 
Je vais devoir créer les corpus de cette manière. C'est la partie chiante mais je m'en charge :-)

### TEMPLATES
Le template pour l'interface web qui sera chargé par Flask

### STATIC
Le élément pour la décoration de l'interface web
