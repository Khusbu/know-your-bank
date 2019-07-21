from flask import jsonify
from app import app
from app.models import Bank, Branch
from flask import render_template


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/search_bank")
def search_bank():
    bank = Bank.query.first()
    return render_template('bank_results.html', bank=bank)


@app.route("/search_branches")
def search_branches():
    branch = Branch.query.first()
    return render_template('branch_results.html', branch=branch)

