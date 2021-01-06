from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello</h1>"

@app.route('/<name>')
def welcome_name(name):
    return "<h1>Hello {}</h1>".format(name)

@app.route('/<int:age>')
def welcome_age(age):
    return "<h1>Hello {}</h1>".format(age)