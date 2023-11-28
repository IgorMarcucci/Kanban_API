from flask import request
from .models import Ticket
from flask_login import login_required
from ..app import app
from .controllers import list_all_tickets_controller, create_ticket_controller, retrieve_ticket_controller, delete_ticket_controller, update_ticket_status_controller, get_tickets_by_dashboard_controller

@app.route("/tickets", methods=['GET','POST'])
@app.login_manager.user_loader
def list_create_tickets():
    if request.method == 'GET': return list_all_tickets_controller()
    if request.method == 'POST': return create_ticket_controller()
    else: return 'Method is Not Allowed'

@app.route("/tickets/<ticket_id>", methods=['GET', 'PUT', 'DELETE'])
@app.login_manager.user_loader
def retrieve_update_destroy_ticket(item_id):
    if request.method == 'GET': return retrieve_ticket_controller(item_id)
    if request.method == 'DELETE': return delete_ticket_controller(item_id)
    else: return 'Method is Not Allowed'

@app.route("/tickets/changeStatus/<ticket_id>", methods=['PUT'])
@app.login_manager.user_loader
def update_ticket_status(ticket_id):
    if request.method == 'PUT': return update_ticket_status_controller(ticket_id)
    else: return 'Method is Not Allowed'

@app.route("/tickets/getTicketsByDashboard/<dashboard_id>", methods=['GET'])
@app.login_manager.user_loader
def get_tickets_by_dashboard(dashboard_id):
    if request.method == 'GET': return get_tickets_by_dashboard_controller(dashboard_id)
    else: return 'Method is Not Allowed'