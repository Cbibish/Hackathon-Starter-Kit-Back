"""Schema for serializing/deserializing a HelloWorldModel"""

from data.user.models.user_model import UserModel
from shared.utils.schema.base_schema import BaseSchema


class UserSchema(BaseSchema):
    class Meta:
        model = UserModel
        load_instance = True
