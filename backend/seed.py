from app import app
from extensions import db
from models import User, AssignedTask, DailyTask
from datetime import date

with app.app_context():
    User.query.delete()
    AssignedTask.delete()
    DailyTask.delete()

    u1 = User(username="jamieab98", password="123456", manager=True, workers_id=[2, 3])
    u2 = User(username="bobbyb44", password="6767", manager=False)
    u3 = User(username="michaelb", password="durrr", manager=False)

    a1 = AssignedTask(assiged_task_description="Find a pookie", owner_id=2)
    a2 = AssignedTask(assigned_task_description="Date your pookie", owner_id=2)
    a3 = AssignedTask(assigned_task_description="Stop bothering your pookie", owner_id=3)
    a4 = AssignedTask(assigned_task_description="Finish putting your bed together", owner_id=3)

    d1 = DailyTask(daily_task_description="Check and reply to emails as necessary", owner_id=1)
    d2 = DailyTask(daily_task_description="Check and reply to emails as necessary", owner_id=2)
    d3 = DailyTask(daily_task_description="Check and reply to emails as necessary", owner_id=3)
    d4 = DailyTask(daily_task_description="Make sure Micahel is working", owner_id=2)
    d5 = DailyTask(daily_task_description="Log your connections in production timer", owner_id=2)
    d6 = DailyTask(daily_task_description="Sweep the kitchen", owner_id=3)
    d7 = DailyTask(daily_task_description="Cout your chickens before they hatch", owner_id=3)