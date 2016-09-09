#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
app = Flask(__name__)  #instancier l'objet app

app.secret_key = 'quelquechosedecompliqueratrouver'


@app.route('/')
def main():
    return render_template('index.html')
    
@app.route('/contact/')
def contact():
    mail = "sven.wauters@mc.be"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


if __name__ == '__main__':
    app.run(debug=True)     #lance l'app en mode debug. Attention, à supprimer quand le site sera disponible sur internet!

