from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS,cross_origin
import base64
import random

app = Flask(__name__)


app.config['SECRET_KEY'] = '//232//'



cors = CORS(app, resources={r"/getimg": {"origins": "*"}})



app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
  return render_template('index.html')



arr = []

@app.route('/getimg',methods=['POST','OPTIONS'])
def getImg():

    data = request.get_json()
    imgdata = base64.b64decode(data['imageFile'])
    filename = 'file{}.jpg'.format(random.randint(0,222))  # I assume you have a way of picking unique filenames
    filePath = 'static/img/'+filename
    with open(filePath, 'wb') as f:
        f.write(imgdata)

    return request.referrer






@app.route('/getallimg')
def getallimg():
    return render_template("disimg.html",arr=arr)


if __name__ == '__main__':
    app.run(debug=True)

