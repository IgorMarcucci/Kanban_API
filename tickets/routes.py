from flask import request
from .models import Ticket
from flask_login import login_required
from ..app import app
from .controllers import list_all_tickets_controller, create_ticket_controller, retrieve_ticket_controller, delete_ticket_controller

@app.route("/tickets", methods=['GET','POST'])
@login_required
def list_create_tickets():
    if request.method == 'GET': return list_all_tickets_controller()
    if request.method == 'POST': return create_ticket_controller()
    else: return 'Method is Not Allowed'

@app.route("/tickets/<ticket_id>", methods=['GET', 'PUT', 'DELETE'])
@login_required
def retrieve_update_destroy_ticket(item_id):
    if request.method == 'GET': return retrieve_ticket_controller(item_id)
    if request.method == 'DELETE': return delete_ticket_controller(item_id)
    else: return 'Method is Not Allowed'
