#/usr/bin/env python
# -*- coding:utf-8 -*-

#Gros problème sur le NA8
#WARNING LES BUGS AU NIVEAU DES ENVIRONNEMENTS VIRTUELS VIENNENT PTET DE LA PREMIERE LIGNE /usr/bin/env python
#ne pas oublier le IGNORE




from flask import Flask, request
from flaskext.mysql import MySQL
import sys
#allocation dynamic dans le path python
#sys.path.append("/home/seb/Fridge_Project/Requetes_web/")
import reqTest
import datetime

#import Partie detection code
sys.path.append("/home/seb/Fridge_Project/Bar_code_Detection/")
import detect_CB
import numpy as np
import cv2
import detect_CB
from time import sleep


mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'seb1'
app.config['MYSQL_DATABASE_PASSWORD'] = 'azop'
app.config['MYSQL_DATABASE_DB'] = 'bddproject'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)  


     
@app.route("/")
def hello():
	return "It's working !!!!!!!!!!!!!!!!!!!!!!!!!!!"
    
@app.route("/addelem/")
def detecte():

	i=0
	now = datetime.datetime.now()
	dateToday = now.strftime("%Y-%m-%d")
	
	conn = mysql.connect()
	cursor = conn.cursor()
	codeBarres = ["5449000000996","5449000014535","3071500419958","3073780591591","3564700014646","3023260005100","3270190021179","3033490968120","3496080210137","3095752126013","3596710061969"]
	
	

	info = reqTest.detection(codeBarres[i])	
	cursor.execute("INSERT  INTO Elem_connu  (id,code_barres,nom,description,image_adress) VALUES (NULL,'"+codeBarres[i]+"','" +info[0]+ "',NULL,NULL )")
	cursor.execute("INSERT INTO Elem_frigo (id,code_barres,date_peremp,date_entree) VALUES (NULL,'" + codeBarres[i] +"',NULL,'"+dateToday+"')")
	i += 1
		
	conn.commit()
	return "ok"
	
@app.route("/elementrant/")
def elementrant():
	now = datetime.datetime.now()
	dateToday = now.strftime("%Y-%m-%d")
	
	device=0
	cap=cv2.VideoCapture(device)
	conn = mysql.connect()
	cursor = conn.cursor()
	while 1:
		#appel de la fonction John pour récupérer le code-barres 
	
		code=detect_CB.detect_CB(cap)
		#print("cdb="+code)
		if code !="NULL":
			print("cdb="+code)
			#code="5449000000996"
			cursor.execute("SELECT code_barres FROM Elem_connu where code_barres='" + code + "'")
			data = cursor.fetchone()
			if data is None:
				info = reqTest.detection(code)	
				cursor.execute("INSERT  INTO Elem_connu  (id,code_barres,nom,description,image_adress) VALUES (NULL,'"+code+"','" +info[0]+ "',NULL,NULL )")
				print("info="+info[0])
				sleep(100)
			cursor.execute("INSERT INTO Elem_frigo (id,code_barres,date_peremp,date_entree) VALUES (NULL,'" + code +"',NULL,'"+dateToday+"')")
			conn.commit()
			sleep(0.5)
			
	
	
if __name__ == "__main__":
	app.run(debug=True)

