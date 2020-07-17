from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def greet():
    return 'welcome'

@app.route('/welcome/home')
def home_greet():
    return 'welcome home'

@app.route('/welcome/back')
def back_greet():
    return 'welcome back'