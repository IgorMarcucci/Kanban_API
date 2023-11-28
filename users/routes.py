from flask import request
from flask_login import login_required
from ..app import app
from .controllers import list_all_users_controller, create_user_controller, retrieve_user_controller, delete_user_controller, login_user_controller, logout_user_controller

@app.route('/login', methods=['POST'])
def login():
    return login_user_controller()

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    return logout_user_controller()

@app.route("/users/create", methods=['POST'])
def create_user():
    return create_user_controller()

@app.route("/users/getUsers", methods=['GET'])
@login_required
def get_users():
    return list_all_users_controller()

@app.route("/users/<user_id>", methods=['GET', 'PUT', 'DELETE'])
@login_required
def retrieve_update_destroy_user(item_id):
    if request.method == 'GET': return retrieve_user_controller(item_id)
    if request.method == 'DELETE': return delete_user_controller(item_id)
    else: return 'Method is Not Allowed'
