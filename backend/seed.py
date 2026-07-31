from app import app
from extensions import db
from models import User, AssignedTask, DailyTask
from datetime import date

with app.app_context():
    User.query.delete()
    AssignedTask.delete()
    DailyTask.delete()

    u = User(username="jamieab98", password="123456")
    