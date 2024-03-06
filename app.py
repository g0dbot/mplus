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
    #app.run(debug=True)
    from gunicorn.app.base import BaseApplication

    class FlaskApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super(FlaskApplication, self).__init__()

        def load_config(self):
            for key, value in self.options.items():
                if key in self.cfg.settings and value is not None:
                    self.cfg.set(key.lower(), value)

        def load(self):
            return self.application

    gunicorn_options = {
        'bind': '0.0.0.0:5000',  # Adjust the host and port as needed
        'workers': multiprocessing.cpu_count() * 2 + 1,
        'threads': 2,
        'loglevel': 'info'
    }

    FlaskApplication(app, gunicorn_options).run()