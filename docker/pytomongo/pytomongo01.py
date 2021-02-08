from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/airdb'
mongo = PyMongo(app)


@app.route('/')
def home():
    posts = mongo.db.air001.find({},{"_id":0})
    return render_template('show001.html', posts=posts)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000,debug=True)