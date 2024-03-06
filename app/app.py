from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from gunicorn.app.base import BaseApplication
import os
import multiprocessing

#init app
app = Flask("m_plus")
basedir = os.path.abspath(os.path.dirname(__file__))

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;

#init db
db = SQLAlchemy(app)

#init ma
ma = Marshmallow(app)

#run server
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return 'Hello WOrld'