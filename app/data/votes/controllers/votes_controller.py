from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from data.votes.models import votesModel
from data.votes.schemas import votesSchema
from shared import db

NAME = "votes"

votes_blueprint = Blueprint(f"{NAME}_votes_blueprint", __name__)


@votes_blueprint.get(f"/votes")
def get_votes():
    """GET route code goes here"""
    import sys 
    id=1
    print(id, file=sys.stderr)
    test = votesModel(opt1="x", opt2="y", opt3="z", opt4="a", cnt1=1, cnt2=5, cnt3=2, cnt4=0)
    print(f"test : {test}", file=sys.stderr)
    db.session.add(test)
    db.session.commit()
    print(f"test : {test}", file=sys.stderr)
    entity: votesModel = db.session.query(votesModel).get(id)
    print(f"entity : {entity}", file=sys.stderr)
    if entity is None:
        return "Nique", 404
    print(f"test : {entity.opt1}", file=sys.stderr)
    return jsonify({'entity': votesSchema().dump(entity)}), 200

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