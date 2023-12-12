from flask import Blueprint, request
from marshmallow import ValidationError

from data.votes.models import votesModel
from data.votes.schemas import votesSchema
from shared import db

NAME = "votes"

votes_blueprint = Blueprint(f"{NAME}_votes_blueprint", __name__)


@votes_blueprint.get(f"/votes/<int:id>")
def get_votes(id: str):
    """GET route code goes here"""
    entity: votesModel = db.session.query(votesModel).get(id)
    if entity is None:
        return "Nique", 404
    return entity.message, 200

@votes_blueprint.post(f"/votes/")
def post_votes():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: votesModel = votesSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid HelloWorldModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return votesSchema().dump(entity), 200