from flask import Flask,jsonify, request,Response
from News import News
import json
import sys
import sqlite3


app = Flask(__name__)

@app.route('/news')
def getNews():
    c = News()
    articles = c.news()
    return Response(json.dumps(articles), mimetype='application/json')
  
@app.route('/register')
def register():
	con = sqlite3.connect('login')
	conn = con.cursor()
	data = {}
	data['status'] = 0 
	query = "INSERT INTO user (fname,lname,phone,location,mail,pass) VALUES ('"+str(request.args.get('fname'))+"','"+str(request.args.get('lname'))+"',"+request.args.get('phone')+",'0','"+str(request.args.get('email'))+"','"+str(request.args.get('pass'))+"')"
	
	conn.execute(query)
	con.commit()
	data['status'] = 1
	con.close()
	return Response(json.dumps(data), mimetype='application/json')

@app.route('/login')
def login():
	conn = sqlite3.connect('login')
	con = conn.cursor()
	data = {}
	data['user'] = ''
	cursor = con.execute("SELECT fname from user where mail='"+str(request.args.get('email'))+"' and pass='"+str(request.args.get('pass'))+"'")
	for row in cursor:	
		data['user'] = row[0]
	conn.close()
	return Response(json.dumps(data), mimetype='application/json')


  
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host="0.0.0.0", port=port)
