from abc import ABC


class BaseEvent(ABC):
    def __init__(self, content: str = ""):
        self.content = content

    @classmethod
    def get_event_name(cls) -> str:
        return cls.__name__


class Type2Event(BaseEvent):
    pass
