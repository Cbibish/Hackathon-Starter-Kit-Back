from flask import Blueprint, request
from marshmallow import ValidationError

from data.hello_world.models import HelloWorldModel
from data.hello_world.schemas import HelloWorldSchema
from shared import db

NAME = "votes"

hello_world_blueprint = Blueprint(f"{NAME}_votes_blueprint", __name__)


@hello_world_blueprint.get(f"/votes/<int:id>")
def get_hello_world(id: str):
    """GET route code goes here"""
    entity: HelloWorldModel = db.session.query(votesModel).get(id)
    if entity is None:
        return "Nique", 404
    return entity.message, 200