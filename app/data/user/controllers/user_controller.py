""" Routes for the endpoint 'hello_world'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.user.models import UserModel
from data.user.schemas import UserSchema
from shared import db

NAME = 'hello_world'

user_blueprint = Blueprint(f"{NAME}_user_blueprint", __name__)


@user_blueprint.get(f"/user/<int:id>")
def get_hello_world(id: str):
    """GET route code goes here"""
    test = UserModel(id=1, message="This is a user test!")
    db.session.add(test)
    entity: UserModel = db.session.query(UserModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@user_blueprint.post(f"/user/")
def post_hello_world():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: UserModel = UserSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid UserModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return UserSchema().dump(entity), 200


@user_blueprint.delete(f"/user/<int:id>")
def delete_hello_world(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@user_blueprint.put(f"/user/<int:id>")
def put_hello_world(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@user_blueprint.patch(f"/user/<int:id>")
def patch_hello_world(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
