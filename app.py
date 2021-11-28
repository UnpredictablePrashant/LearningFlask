from flask import Flask, app
from flask.templating import render_template

app = Flask(__name__)


#First Flask code to display Hello World
@app.route('/test')
def hello_world():
    return "Hello World"


#Create an index page
@app.route('/')
def indexPage():
    return render_template('index.html')


#creating login page
@app.route('/login/')
def loginPage():
    return render_template('login.html')


#creating register page
@app.route('/register/')
def registerPage():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)