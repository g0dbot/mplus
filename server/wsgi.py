from flask import Flask
from App.database import db, get_migrate
from App.main import create_app

app = create_app()
migrate = get_migrate(app)