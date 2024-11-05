import requests

import requests
from flask import Flask, request
from flask_cors import CORS, cross_origin

import pyjokes

url = 'http://localhost:8080/'


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/get")
def hello_world():
    response = requests.get(url,headers={'Content-type': "application/json"}, stream=True)
    data =response.raw.read()
    print(data,response)
    return data

#
# curl -v -H "Content-Type: application/json" -d "{\"heads\":6 }" -X POST "http://localhost:5000/compute"
#
@app.route("/joke", methods=['GET', 'POST'])
def store_score():
    myData = request.json
    print(str(request.json))
    print(request);

    response = requests.get(url + "joke", headers={'Content-type': "application/json; charset=UTF-8"}, json=myData, stream=True)
    print(str(response.raw.read()))
    return "good!"

if __name__=="__main__":
    app.run(port=5000, debug=True)
