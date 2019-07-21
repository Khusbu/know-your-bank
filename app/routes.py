from flask import jsonify
from app import app
from app.models import Bank


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/get_first")
def get_first():
    return jsonify(Bank.query.first().serialize())