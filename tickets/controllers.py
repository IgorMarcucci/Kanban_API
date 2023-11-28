from flask import request, jsonify
import uuid

from .. import db
from .models import Ticket

def list_all_tickets_controller():
    tickets = Ticket.query.all()
    response = []
    for ticket in tickets: response.append(ticket.toDict())
    return jsonify(response)

def create_ticket_controller():
    request_form = request.get_json()

    id = str(uuid.uuid4())
    new_ticket = Ticket(
                    id           = id,
                    name         = request_form['name'],
                    description = request_form['description'],
                    dashboard_id = request_form['dashboard_id']
                    )
    db.session.add(new_ticket)
    db.session.commit()

    response = Ticket.query.get(id).toDict()
    return jsonify(response)

def retrieve_ticket_controller(ticket_id):
    response = Ticket.query.get(ticket_id).toDict()
    return jsonify(response)

def delete_ticket_controller(ticket_id):
    Ticket.query.filter_by(id=ticket_id).delete()
    db.session.commit()

    return ('Ticket with Id "{}" deleted successfully!').format(ticket_id)
