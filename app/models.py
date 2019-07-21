from app import db


class Bank(db.Model):
    __tablename__ = 'banks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    branches = db.relationship('Branch', backref='bank', lazy=True)

    def __repr__(self):
        return '<{}: {}>'.format(self.id, self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Branch(db.Model):
    __tablename__ = 'branches'

    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=False)
    ifsc = db.Column(db.String(), primary_key=True)
    branch = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())
    district = db.Column(db.String())
    state = db.Column(db.String())

    def __repr__(self):
        return '''Bank Id: {}
                  IFSC: {}
                  Branch: {}
                  Address: {}
                  City: {}
                  District: {}
                  State: {}'''.format(self.bank_id,
                                      self.ifsc,
                                      self.branch,
                                      self.address,
                                      self.city,
                                      self.district,
                                      self.state)

    def serialize(self):
        return {
            'bank_id': self.bank_id,
            'ifsc': self.ifsc,
            'branch': self.branch,
            'address': self.address,
            'city': self.city,
            'district': self.district,
            'state': self.state
        }