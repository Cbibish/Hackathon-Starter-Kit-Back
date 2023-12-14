#""" Routes for the endpoint 'hello_world'"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from data.user.models.user_model import UserModel
from flask import Blueprint, request
from marshmallow import ValidationError

from data.user.models import UserModel
from data.user.schemas import UserSchema
from shared import db

NAME = 'user'

user_blueprint = Blueprint(f"{NAME}_user_blueprint", __name__)


@user_blueprint.get(f"/user/<int:id>")
def get_user(id: str):
    """GET route code goes here"""
    entity: UserModel = db.session.query(UserModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return jsonify({'entity': UserSchema().dump(entity)}), 200

@user_blueprint.get("/username/<string:name>")
def get_user_by_name(name: str):
    """GET route to retrieve user by name"""
    entity: UserModel = db.session.query(UserModel).filter_by(username=name).first()

    if entity is None:
        return "Goodbye, World.", 404

    return jsonify({'entity': UserSchema().dump(entity)}), 200

@user_blueprint.post(f"/login")
def login():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: UserModel = UserSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid UserModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return UserSchema().dump(entity), 200

@user_blueprint.post(f"{NAME}/register")
def register():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: UserModel = UserSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid UserModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return UserSchema().dump(entity), 200