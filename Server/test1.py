#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request
app = Flask(__name__)
app.debug=True

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
	if request.method == 'GET':
		return " afficher le formulaire"
		
	else:
		return "traiter les données reçues \n afficher : Merci de m'avoir laissé un message !"
		


if __name__ == '__main__':
	app.run()

