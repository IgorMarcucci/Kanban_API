from flask import jsonify, request
from .models import Ticket
from ..app import app

@app.route("/tickets", methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify({'id': tickets.id} for ticket in tickets)