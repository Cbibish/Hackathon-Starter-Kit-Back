from flask import Blueprint, request

from data.authentification.phone.schema import LoginValidationSchema
from data.authentification.user.schema import UserSchema
from shared.authentification.managers import PhoneJwtManager

NAME = "phone_auth"
blueprint = Blueprint(NAME + "_blueprint", __name__)

jwt_manager = PhoneJwtManager()

login_validation_schema = LoginValidationSchema()
user_schema = UserSchema()
send_sms_validation_schema = UserSchema(only=['phone'])


@blueprint.post(f'/{NAME}/register')
def register():
    data = request.get_json()
    new_user = user_schema.load(data)
    return jwt_manager.register_profile(new_user)


@blueprint.post(f'/{NAME}/send_sms')
def send_msg():
    data = request.get_json()
    send_sms_validation_schema.validate(data)
    if jwt_manager.send_phone_msg(data["phone"]):
        return 'ok'
    return 'error'


@blueprint.post(f'/{NAME}/login')
def login():
    data = request.get_json()
    login_validation_schema.validate(data)
    token = jwt_manager.authenticate_by_phone(data['phone'], data['code'])
    if token is None:
        return 'error'
    return token
