import flask
from pymongo import MongoClient


#client = MongoClient('mongodb://mongo_db')
DOMAIN = '0.0.0.0'
PORT = 27017

client = MongoClient(
    host= [str(DOMAIN) + ':' + str(PORT)]
)

db = client['practica-4']
collection = db['people']

app = flask.Flask(__name__)

@app.route('/')
def home():
    return '<h1>It\'s working!</h1>'

@app.route('/people')
def get_people():
    result = []
    for element in collection.find():
        result.append(element)
        print(element)
    return result

@app.route('/people/<id>')
def get_person(id):
    result = collection.find_one({'id': str(id)})
    return result
    
app.run()