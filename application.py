from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Mukul welcome to azure webapp!</h1>"