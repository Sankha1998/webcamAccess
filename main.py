import json
from flask import Flask, render_template, request, redirect, url_for, jsonify,send_file
from flask_cors import CORS,cross_origin
from database import db,Imgdetails
import base64
import random
import datetime
from io import BytesIO

app = Flask(__name__)

with open('config.json', 'r') as c:
    params = json.load(c)['params']

app.config['SECRET_KEY'] = '//232//'


cors = CORS(app, resources={r"/getimg": {"origins": "*"}})



app.config['CORS_HEADERS'] = 'Content-Type'

local_server = True
app.config['JSON_SORT_KEYS'] = False

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db.init_app(app)

@app.route('/')
def home():
  return render_template('index.html')



@app.route('/getimg',methods=['POST','OPTIONS'])
def getImg():

    data = request.get_json()

    fileName = 'testing{}'.format(random.randint(0,1024))
    data = Imgdetails(fileName=fileName, imgData=data['imageFile'],time= datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    db.session.add(data)
    db.session.commit()

    return request.referrer



@app.route('/blob/media')
def media():
    files = Imgdetails.query.order_by(Imgdetails.slno.desc()).all()
    return render_template('media.html',files=files)






if __name__ == '__main__':
    app.run(debug=True)

