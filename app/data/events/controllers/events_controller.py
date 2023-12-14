from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from data.events.models import eventsModel
from data.events.schemas import eventsSchema
from shared import db

NAME = "events"

events_blueprint = Blueprint(f"{NAME}_events_blueprint", __name__)


@events_blueprint.get(f"/events/<int:id>")
def get_events(id: str):
    """GET route code goes here"""
    entity: eventsModel = db.session.query(eventsModel).get(id)
    if entity is None:
        return "Nique", 404
    return jsonify({'entity': eventsSchema().dump(entity)}), 200

@events_blueprint.post(f"/events/")
def post_events():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: eventsModel = eventsSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid HelloWorldModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return eventsSchema().dump(entity), 200