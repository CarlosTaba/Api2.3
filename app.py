from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) ## To allow direct AJAX calls

@app.route('/datos', methods=['GET'])
def home():
    r = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=19.54&lon=-96.91')

    return r.json()

if __name__ == '__main__':
   app.run(debug = True)