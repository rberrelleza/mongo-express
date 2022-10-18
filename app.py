import os

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb://{os.environ['MONGO_ROOT_USERNAME']}:{os.environ['MONGO_ROOT_PASSWORD']}@mongo:27017/{os.environ['MONGO_DATABASE']}?authSource=admin"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return f" Hello, Okteto! Your MongoDB info: {mongo.db.command('buildinfo')}" 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)