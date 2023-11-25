from flask import request, jsonify
import uuid

from .. import db
from .models import Dashboard


def list_all_dashboards_controller():
    dashboards = Dashboard.query.all()
    response = []
    for dashboard in dashboards: response.append(dashboard.toDict())
    return jsonify(response)

def create_dashboard_controller():
    request_form = request.form.to_dict()

    id = str(uuid.uuid4())
    new_dashboard = Dashboard(
                    id           = id,
                    name         = request_form['name'],
                    price        = float(request_form['price']),
                    description  = request_form['description'],
                    image_link   = request_form['image_link'],
                    account_id   = request_form['account_id'],
                    )
    db.session.add(new_dashboard)
    db.session.commit()

    response = Dashboard.query.get(id).toDict()
    return jsonify(response)

def retrieve_dashboard_controller(dashboard_id):
    response = Dashboard.query.get(dashboard_id).toDict()
    return jsonify(response)

# def update_dashboard_controller(dashboard_id):
#     request_form = request.form.to_dict()
#     dashboard = Dashboard.query.get(dashboard_id)

#     dashboard.name        = request_form['name']
#     dashboard.price       = float(request_form['price'])
#     dashboard.description = request_form['description']
#     dashboard.image_link  = request_form['image_link']
#     dashboard.account_id  = request_form['account_id']
#     db.session.commit()

#     response = Dashboard.query.get(dashboard_id).toDict()
#     return jsonify(response)

def delete_dashboard_controller(dashboard_id):
    Dashboard.query.filter_by(id=dashboard_id).delete()
    db.session.commit()

    return ('Dashboard with Id "{}" deleted successfully!').format(dashboard_id)
