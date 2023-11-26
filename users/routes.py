from flask import jsonify, request

from ..app import app

from .controllers import list_all_users_controller, create_user_controller, retrieve_user_controller, delete_user_controller

@app.route("/users", methods=['GET','POST'])
def list_create_users():
    if request.method == 'GET': return list_all_users_controller()
    if request.method == 'POST': return create_user_controller()
    else: return 'Method is Not Allowed'

@app.route("/users/<user_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_user(item_id):
    if request.method == 'GET': return retrieve_user_controller(item_id)
    if request.method == 'DELETE': return delete_user_controller(item_id)
    else: return 'Method is Not Allowed'
