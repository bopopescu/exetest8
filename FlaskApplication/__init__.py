from flask import Flask, render_template
from flask import request, redirect

from models import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():
    input_a = int(request.form['input_a'])
    input_b = int(request.form['input_b'])

    f = Flight()

    calc_a = f.sum(input_a, input_b)
    calc_b = f.multiply(input_a, input_b)

    return render_template('result.html', **locals())

# @app.route('/tst', methods=['POST'])
# def tst():
#     easting = int(request.form['easting'])
#     northing = int(request.form['northing'])
#     f = Flight()
#     result = f.test(easting, northing)
#     return render_template('gridResult.html', **locals())

@app.route('/pc', methods=['POST'])
def pc():
    pc = str(request.form['pc'])
    f = Flight()
    result = f.test(pc)
    return render_template('gridResult.html', **locals())
if __name__ == "__main__":
    app.run(debug=True)