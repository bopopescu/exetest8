from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Ben Mayo"
    name = "Ben"
    return render_template('index.html', author=author, name=name)
    
@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return email

@app.route('/passVar', methods = ['POST'])
def runPassVar():
    varToPass = request.form['varBox']
    return varToPass

if __name__ == "__main__":
    app.run()
