from flask import Flask
from flask_cors import CORS, cross_origin
import warnings
warnings.filterwarnings('ignore')
import random
import hashlib
import urllib.request


app = Flask(__name__)
from flask import Flask
from flask import request
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def predict_cancer(SOURCE_URL):

    try:
        urllib.request.urlretrieve(SOURCE_URL, "/home/ec2-user/test/Melanoma/m.jpg")
        prediction = Prediction()
        #pred_class contains 'Melanoma' or 'Not Melanoma'
        pred_class = prediction.predict_class()
        pic_gen = Pic_gen()
        pic_gen.generate_pics()
    except Exception as e:
        print('Error')
        print(e)
        return 'An error has been encountered'
    

@app.route('/predict_cancer_api', methods=['POST'])
@cross_origin()
def predict_cancer_api():
    try:
        content = request.json
        predict_cancer(content['SOURCE_URL'])
        # return predict_price(content['LOCATION'], content['TYPE'], content['TRANSACTION'], int(content['AREA']), int(content['BEDROOMS']), int(content['BATHROOMS']))
    except Exception as e:
        print(request)
        print(e.__class__.__name__)
        print(e)
        return "Error in request parameters !"

app.run(host='0.0.0.0', port=2412)
