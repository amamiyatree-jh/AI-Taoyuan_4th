from flask import Flask, request, render_template
import pymysql, json, time
from flask_pymongo import PyMongo

db = pymysql.connect(host="localhost", user="root", password="admin@Qq13579", db="test001")

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/airdb'
mongo = PyMongo(app)

@app.route('/')
def someName():
	cursor = db.cursor()
	sql = "SELECT * FROM `air001`"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template('show001.html', results=results) 

@app.route('/mysqlgetdata', methods=['GET'])
def mysqlgetdata():
	cursor = db.cursor()
	sql = "SELECT * FROM air001 WHERE %s LIKE '%%%%%s%%%%'" % (request.args['title'], request.args['words']) 
	cursor.execute(sql)
	results = cursor.fetchall()
	
	sql2 = "SELECT column_name FROM information_schema.columns WHERE table_name='air001'"
	cursor.execute(sql2)
	tb_title01 = cursor.fetchall()

	T1 = list(results)
	T2 = list(tb_title01)
	T2[11] = 'PM2_5'
	T2[18] = 'PM2_5_AVG'

	Ti_Buffer01 = []
	for r in T2:
		a = str(r).replace("('", "").replace("',)", "")
		Ti_Buffer01.append(a)
	
	Re_Buffer01 = []
	for r in T1:
		Re_Buffer02 = []
		for c in r:
			a = str(c).replace("Decimal", "").replace("('", "").replace("')", "")
			Re_Buffer02.append(a)
		Re_Buffer01.append(Re_Buffer02)
	
	d={}
	for r in Re_Buffer01:
		for i in range(0,len(r)):
			d.setdefault(Ti_Buffer01[i],[])
			d[Ti_Buffer01[i]].append(r[i])

	a = d.keys()
	millis = int(round(time.time() * 1000))#通過把秒轉換毫秒的方法獲得13位的時間戳round()是四捨五入。
	file_name = './log/' + str(millis) + '_' + request.args['title'] + '_' + request.args['words'] + '.json'
	with open(file_name.encode('utf-8'),"w",encoding='utf-8') as f:
		json.dump(d,f,ensure_ascii=False,indent=4)

	mongo.db.airsearchlog.insert(d)
	
	return render_template('show.html', results=results, tb_title01=tb_title01 ) 

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000,debug=True)

# http://127.0.0.1:5000/mysqlgetdata?title=County&words=臺
# http://127.0.0.1:5000/mysqlgetdata?title=Status&words=敏感
# http://127.0.0.1:5000/mysqlgetdata?title=Pollutant&words=細懸浮
# http://127.0.0.1:5000/mysqlgetdata?title=Status&words=對敏感族群不健康
# http://127.0.0.1:5000/mysqlgetdata?title=teName&words=彰化