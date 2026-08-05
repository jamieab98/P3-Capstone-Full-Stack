from extensions import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(225), nullable=False)
    manager = db.Column(db.Boolean, nullable=False)
    workers_id = db.Column(db.JSON, default=list, nullable=True)
    assigned_tasks = db.relationship("AssignedTask", backref="user", lazy=True)
    daily_tasks = db.relationship("DailyTask", backref="user", lazy=True)

class AssignedTask(db.Model):
    __tablename__ = "assigned_tasks"
    id = db.Column(db.Integer, primary_key=True)
    assigned_task_description = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    completion_status = db.Column(db.Boolean, default=False)

class DailyTask(db.Model):
    __tablename__ = "daily_tasks"
    id = db.Column(db.Integer, primary_key=True)
    daily_task_description = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    completion_status = db.Column(db.Boolean, default=False)
    dates_completed = db.Column(db.JSON, default=list)