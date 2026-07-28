from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    aTasks = db.relationship("AssignedTask", backref="user", lazy=True)

class AssignedTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aTaskDescription = db.Column(db.String, nullable=False)
    ownerId = db.Column(db.Integer, db.Foreignkey("user.id"), nullable=False)