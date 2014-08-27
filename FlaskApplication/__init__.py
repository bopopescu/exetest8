from flask import Flask
from flask import render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html",
        )
        
@app.route('/home', methods=['POST'])
def home():
    return render_template('home.html',
    )

@app.route('/away', methods=['POST'])
def away():
    return render_template('away.html',
    )
    
@app.route('/nearby', methods=['POST'])
def nearby():
    return render_template('nearby.html',
    )
    
app.debug = True
if __name__ == "__main__":
    app.run()