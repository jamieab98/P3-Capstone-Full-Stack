from app import app
from extensions import db
from models import User, AssignedTask
from datetime import date

with app.app_context():
    User.query.delete()
    AssignedTask.query.delete()

    u1 = User(username="jamieab98", password="123456", manager=True, workers_id=[2, 3])
    u2 = User(username="bobbyb44", password="6767", manager=False)
    u3 = User(username="michaelb", password="durrr", manager=False)

    a1 = AssignedTask(assigned_task_description="Find a pookie", owner_id=2)
    a2 = AssignedTask(assigned_task_description="Date your pookie", owner_id=2)
    a3 = AssignedTask(assigned_task_description="Stop bothering your pookie", owner_id=3)
    a4 = AssignedTask(assigned_task_description="Finish putting your bed together", owner_id=3)
    a5 = AssignedTask(assigned_task_description="Complete this assignment", owner_id=1)

    db.session.add_all([u1, u2, u3, a1, a2, a3, a4, a5])
    db.session.commit()