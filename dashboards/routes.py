from flask import request
from ..app import app
from .controllers import list_all_dashboards_controller, create_dashboard_controller, retrieve_dashboard_controller, delete_dashboard_controller, get_dashboard_by_user_id_controller

@app.route("/dashboards", methods=['GET','POST'])
@app.login_manager.user_loader
def list_create_dashboards():
    if request.method == 'GET': return list_all_dashboards_controller()
    if request.method == 'POST': return create_dashboard_controller()
    else: return 'Method is Not Allowed'

@app.route("/dashboards/<dashboard_id>", methods=['GET', 'PUT', 'DELETE'])
@app.login_manager.user_loader
def retrieve_update_destroy_dashboard(item_id):
    if request.method == 'GET': return retrieve_dashboard_controller(item_id)
    if request.method == 'DELETE': return delete_dashboard_controller(item_id)
    else: return 'Method is Not Allowed'

@app.route("/dashboards/getDashboard/<user_id>", methods=['GET'])
@app.login_manager.user_loader
def get_dashboard_by_user_id(user_id):
    if request.method == 'GET': return get_dashboard_by_user_id_controller(user_id)
    else: return 'Method is Not Allowed'
