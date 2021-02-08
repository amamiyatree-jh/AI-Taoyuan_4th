from flask import Flask, request, render_template
import pymysql

db = pymysql.connect(host="localhost", user="root", password="admin@Qq13579", db="test001")

app = Flask(__name__)
#api = Api(app)

@app.route('/')
def someName():
	cursor = db.cursor()
	sql = "SELECT * FROM `air001`"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template('show001.html', results=results) 

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000,debug=True)