import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/get_first")
def get_first():
    from models import Bank
    return jsonify(Bank.query.first().serialize())


if __name__ == '__main__':
    app.run()