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

api.add_resource(Home, "/")
api.add_resource(Login, "/login")
api.add_resource(UserData, "/userdata/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)