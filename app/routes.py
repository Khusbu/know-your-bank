from flask import request, render_template
from app import app
from app.models import Bank, Branch


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/search_branch")
def search_branch():
    ifsc = request.args.get('ifsc').upper()
    branch = Branch.query.filter_by(ifsc=ifsc).first()
    return render_template('branch_results.html', branch=branch)


@app.route("/search_branches")
def search_branches():
    bank_name = request.args.get('bank_name').upper()
    city = request.args.get('city').upper()
    bank = Bank.query.filter_by(name=bank_name).first()
    branches = Branch.query.filter_by(bank_id=bank.id, city=city) if bank else None
    total = branches.count() if branches else 0
    return render_template('branches_results.html', branches=branches, total=total)

