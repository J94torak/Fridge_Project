#/usr/bin/env python
# -*- coding:utf-8 -*-

#WARNING LES BUGS AU NIVEAU DES ENVIRONNEMENTS VIRTUELS VIENNENT PTET DE LA PREMIERE LIGNE /usr/bin/env python
from flask import Flask, request
from flaskext.mysql import MySQL
import requete 

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'azop'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/Authenticate/")
def Authenticate():
	
    username = request.args.get('UserName')
    password = request.args.get('Password')
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO User (userId,userName,password) VALUES ('','John', 'John')")
    cursor.execute("INSERT INTO User (userId,userName,password) VALUES ('','Jean', 'Jean')")
    cursor.execute("INSERT INTO User (userId,userName,password) VALUES ('','Maria', 'Maria')")
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    conn.commit()
    data = cursor.fetchone()
    if data is None:
    	return "Username or Password is wrong"
    else:
    	return "Logged in successfully"
    	
    
     
     
@app.route("/")
def hello():
    return "It's working !!!!!!!!!!!!!!!!!!!!!!!!!!!"
    
#@app.route("/detecte")
#def detecte():
    #codeBarres = requete.detection(5449000000996)
 	#return codeBarres[0]+codeBarres[1]+codeBarres[2]
 	
if __name__ == "__main__":
    app.run(host="192.168.1.38", port=int("80"))

