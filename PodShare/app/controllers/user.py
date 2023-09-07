from flask import request
from app import bcrypt, db
from app.models.user import User
from app.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from app.utils.errors import CustomError
from app.utils.response import generate_response


class UserAuthentication:
    def login(self):
        pass
    def logout(self):
        pass
    def login_required(self):
        # a function decorator
        pass


class UserController:
    def create_user(self):
        user = None
        try:
            user = self.find_user()
        except CustomError:
            pass
        if user:
            raise CustomError("User already Exists", HTTP_409_CONFLICT)
        new_user = {
            'fullname': request.json.get('fname'),
            'username': request.json.get('uname'),
            'email': request.json.get('email'),
            'password': request.json.get('password')
        }
        new_user['password'] = bcrypt.generate_password_hash(new_user['password']).decode()
        new_user = User(**new_user)
        db.session.add(new_user)
        db.session.commit()
        return generate_response(new_user.to_json(), "User created", HTTP_201_CREATED)
    
    def find_user(self):
        user = db.session.query(User).filter_by(username=request.json.get('uname')).first()
        if not user:
            raise CustomError('User not found', 404)
        return user
