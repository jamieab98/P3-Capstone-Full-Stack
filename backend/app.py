from flask import Flask, request
from flask_restful import Api, Resource
from extensions import migrate, db, cors

app = Flask(__name__)
app.secret_key = "super-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
cors(app)
migrate.init_app(app, db)

from models import User, AssignedTask, DailyTask

api = Api(app)

class Home(Resource):
    def get(self):
        return {'message': 'The backend is running'}

class Login(Resource):
    def post(self):
        data = request.json
        user = User.query.filter_by(username=data.get('username')).first()
        if not user or data.get('password') != user.password:
            return{'error': 'Failed Login Attempt'}, 401
        return(user.to_dict())

class UserData(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        assigned_tasks = AssignedTask.query.filter_by(owner_id=id).all()
        daily_tasks = DailyTask.query.filter_by(owner_id=id).all()
        atasks = []
        dtasks = []
        for task in assigned_tasks:
            atasks.append(task.to_dict())
        for task in daily_tasks:
            dtasks.append(task.to_dict())
        userdata = {
            'id': user.id,
            'username': user.username,
            'manager': user.manager,
            'workers_id': user.workers_id,
            'assigned_tasks': atasks,
            'daily_tasks': dtasks
        }
        return(userdata)

class UserTasks(Resource):
    def get(self, id):
        user_assigned_tasks = AssignedTask.query.filter_by(owner_id=id).all()
        user_daily_tasks = DailyTask.query.filter_by(owner_id=id).all()
        user_tasks = []
        for t in user_assigned_tasks:
            user_tasks.append(t.to_dict())
        for t in user_daily_tasks:
            user_tasks.append(t.to_dict())
        return(user_tasks)

class ChangeCompletion(Resource):
    def patch(self, id):
        data = request.json
        if data['type']=='daily':
            task = DailyTask.query.filter_by(id=id).first()
        else:
            task = AssignedTask.query.filter_by(id=id).first()
        if task.completion_status == True:
            task.completion_status = False
        else:
            task.completion_status = True
        db.session.commit()
        return(task.to_dict()), 200

class AssignTask(Resource):
    def post(self, id):
        data = request.json
        assigner = User.query.filter_by(id=id).first()
        if not assigner.manager:
            return {'error': 'User is not a manager and cannot assign tasks'}, 400
        if int(data['ownerID']) not in assigner.workers_id:
            return {'error': 'User is not a manager of the employee and thus cannot assign an assignment to this employee'}, 400
        newTask = AssignedTask(assigned_task_description=data['description'], owner_id=data['ownerID'])
        db.session.add(newTask)
        db.session.commit()
        return(newTask.to_dict()), 200

api.add_resource(Home, "/")
api.add_resource(Login, "/login")
api.add_resource(UserData, "/userdata/<int:id>")
api.add_resource(UserTasks, "/usertasks/<int:id>")
api.add_resource(ChangeCompletion, "/changecompletion/<int:id>")
api.add_resource(AssignTask, "/assigntask/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)