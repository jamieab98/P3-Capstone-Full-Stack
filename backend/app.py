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

from models import User, AssignedTask

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
        atasks = []
        for task in assigned_tasks:
            atasks.append(task.to_dict())
        userdata = {
            'id': user.id,
            'username': user.username,
            'manager': user.manager,
            'workers_id': user.workers_id,
            'assigned_tasks': atasks,
        }
        return(userdata)

class UserTasks(Resource):
    def get(self, id):
        user_assigned_tasks = AssignedTask.query.filter_by(owner_id=id).all()
        user_tasks = []
        for t in user_assigned_tasks:
            user_tasks.append(t.to_dict())
        return(user_tasks)

class ChangeCompletion(Resource):
    def patch(self, id):
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
            print(assigner.to_dict())
            return {'error': 'User is not a manager of the employee and thus cannot assign an assignment to this employee'}, 400
        newTask = AssignedTask(assigned_task_description=data['description'], owner_id=data['ownerID'])
        db.session.add(newTask)
        db.session.commit()
        return(newTask.to_dict()), 200

class CreateUser(Resource):
    def post(self, id):
        manager = User.query.filter_by(id=id).first()
        if not manager.manager:
            return{'error': 'Employee is not a manager can cannot onboard'}, 400
        data = request.json
        users = User.query.all()
        usernames = []
        for u in users:
            usernames.append(u.username)
        if not data['username']:
            return{'error': 'Username field must be filled out'}, 400
        if data['username'] in usernames:
            return{'error': 'Username must be unique'}, 400
        if data['password'] != data['confirm_password']:
            return{'error': 'Passwords do not match'}, 400
        new_user = User(username=data['username'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        new_user_id = User.query.filter_by(username=data['username']).first().id
        manager.workers_id.append(new_user_id)
        db.session.commit()
        return(new_user.to_dict()), 200

class DeleteTask(Resource):
    def delete(self, id):
        data = request.json
        task = AssignedTask.query.filter_by(id=id).first()
        employee = User.query.filter_by(id=task.owner_id).first()
        manager = User.query.filter(User.workers_id.contains(employee.id)).first()
        print(manager.to_dict())
        if manager.password != data['manager_password']:
            print(manager.username)
            return{'error': 'incorrect password'}, 400
        db.session.delete(task)
        db.session.commit()
        return {'message': 'task has been deleted'}, 200

api.add_resource(Home, "/")
api.add_resource(Login, "/login")
api.add_resource(UserData, "/userdata/<int:id>")
api.add_resource(UserTasks, "/usertasks/<int:id>")
api.add_resource(ChangeCompletion, "/changecompletion/<int:id>")
api.add_resource(AssignTask, "/assigntask/<int:id>")
api.add_resource(CreateUser, "/createuser/<int:id>")
api.add_resource(DeleteTask, "/deletetask/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)