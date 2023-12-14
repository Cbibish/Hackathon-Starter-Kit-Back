class eventsService:
    @staticmethod
    def is_greeting(value: str) -> bool:
        value_lowercase = value.lower()
        return "events" in value_lowercase
