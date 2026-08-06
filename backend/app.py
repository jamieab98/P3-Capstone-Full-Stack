from flask import Flask, request, session
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

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return{'error': 'Not logged in'}, 401
        user = User.query.filter_by(id=user_id).first()
        return user.to_dict(), 200

class Login(Resource):
    def post(self):
        data = request.json
        user = User.query.filter_by(username=data.get('username')).first()
        if not user or data.get('password') != user.password:
            return{'error': 'Failed Login Attempt'}, 401
        session['user_id'] = user.id
        return(user.to_dict())

class UserData(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        return(user.to_dict())

api.add_resource(Home, "/")
api.add_resource(CheckSession, "/checksession")
api.add_resource(Login, "/login")
api.add_resource(UserData, "/userdata/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)