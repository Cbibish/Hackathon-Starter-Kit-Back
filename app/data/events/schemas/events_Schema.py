"""Schema for serializing/deserializing a HelloWorldModel"""

from data.events.models.events_Model import eventsModel
from shared.utils.schema.base_schema import BaseSchema


class eventsSchema(BaseSchema):
    class Meta:
        model = eventsModel
        load_instance = True
