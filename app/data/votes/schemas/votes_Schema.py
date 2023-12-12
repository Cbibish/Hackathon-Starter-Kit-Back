"""Schema for serializing/deserializing a HelloWorldModel"""

from data.votes.models.votes_Model import votesModel
from shared.utils.schema.base_schema import BaseSchema


class votesSchema(BaseSchema):
    class Meta:
        model = votesModel
        load_instance = True
