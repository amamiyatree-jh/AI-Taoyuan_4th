import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


app.run(host="0.0.0.0", port=5000)