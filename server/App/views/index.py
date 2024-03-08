from flask import Blueprint, jsonify

index_views = Blueprint('index_views', __name__)

@index_views.route('/', methods=['GET'])
def index_page():
    return ("Hi")