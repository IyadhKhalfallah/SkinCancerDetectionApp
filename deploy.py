from flask import Flask
from model import *
from flask import request
app = Flask(__name__)

@app.route('/api/question', methods = ['POST'])
def answerFunction():
	question = request.args.get('question', '')
	return answer([question])[0][0]

@app.route('/api/question', methods = ['GET'])
def answerFunctionGET():
	return "HELLO WORLD"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
