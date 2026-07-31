from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    manager = db.Column(db.Boolean, nullable=False)
    workers = db.Column(db.JSON, default=list)
    assigned_tasks = db.relationship("AssignedTask", backref="user", lazy=True)
    daily_tasks = db.relationship("DailyTask", backref="user", lazy=True)

class AssignedTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assigned_task_description = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.Foreignkey("user.id"), nullable=False)
    completion_status = db.Column(db.Boolean, nullable=False)

class DailyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    daily_task_description = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.Foreignkey("user.id"), nullable=False)
    completion_status = db.Column(db.Boolean, nullable=False)
    dates_completed = db.Column(db.JSON, default=list)