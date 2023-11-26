from flask import request, jsonify
import uuid
import bcrypt
from .. import db
from .models import User
from flask_login import login_user, logout_user


def list_all_users_controller():
    users = User.query.all()
    response = []
    for user in users: response.append(user.toDict())
    return jsonify(response)

def create_user_controller():
    request_form = request.form.to_dict()

    id = str(uuid.uuid4())
    new_user = User(
                    id           = id,
                    name         = request_form['name'],
                    username = request_form['username'],
                    email = request_form['email'],
                    password = bcrypt.hashpw(request_form['password'], 5),
                    specialty = request_form['specialty'],
                    working_area = request_form['working_area'],
                    )
    db.session.add(new_user)
    db.session.commit()

    response = User.query.get(id).toDict()
    return jsonify(response)

def retrieve_user_controller(user_id):
    response = User.query.get(user_id).toDict()
    return jsonify(response)

def delete_user_controller(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return ('User with Id "{}" deleted successfully!').format(user_id)

def login_user(user, data):
    if user and user.password == data['password']:
        login_user(user)
        return jsonify({'message': 'User logged in'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

def logout_user():
    logout_user()
    return jsonify({'message': 'User logged out'}), 200
