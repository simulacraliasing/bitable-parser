from .event import Event as Event
from lark_oapi.core.construct import init as init

class UnsubscribeEventRequestBody:
    events: list[Event] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UnsubscribeEventRequestBodyBuilder: ...

class UnsubscribeEventRequestBodyBuilder:
    def __init__(self) -> None: ...
    def events(self, events: list[Event]) -> UnsubscribeEventRequestBodyBuilder: ...
    def build(self) -> UnsubscribeEventRequestBody: ...
