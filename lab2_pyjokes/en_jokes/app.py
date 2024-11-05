from flask import request, Flask
import json, socket
import computeEngine 
import pyjokes

#import hashlib,random


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is backend  ! ' + str(socket.gethostname()) + ' \n'

@app.route("/joke", methods=["GET"])
def joke():
	joke = pyjokes.get_joke(language="en")
	#joke = "... running dry here"
	retDict= {}
	retDict['joke'] = joke
	return json.dumps(retDict)

@app.route("/compute", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    bc = computeEngine.BackendCompute(hostName)    
    bc.processPRandomSeed()
    
    limit = int(request.json['heads'])
    print("limit: ", limit)

    total_flips = bc.flipCoinsUntil(int(limit))
    returnDictionary = {}
    returnDictionary["hostName"] = hostName
    returnDictionary["total_flips"] = total_flips
    returnDictionary["heads"] = request.json['heads']
    
    return json.dumps(returnDictionary)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
