from extensions import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(225), nullable=False)
    manager = db.Column(db.Boolean, nullable=False)
    workers_id = db.Column(db.JSON, default=list, nullable=True)
    assigned_tasks = db.relationship("AssignedTask", backref="user", lazy=True)

    def to_dict(self):
        return{
            "id": self.id,
            "username": self.username,
            "manager": self.manager,
            "workers_id": self.workers_id
        }

class AssignedTask(db.Model):
    __tablename__ = "assigned_tasks"
    id = db.Column(db.Integer, primary_key=True)
    assigned_task_description = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    completion_status = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return{
            "id": self.id,
            "assigned_task_description": self.assigned_task_description,
            "owner_id": self.owner_id,
            "completion_status": self.completion_status
        }