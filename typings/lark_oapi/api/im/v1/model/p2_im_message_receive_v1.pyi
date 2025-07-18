from .event_message import EventMessage as EventMessage
from .event_sender import EventSender as EventSender
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ImMessageReceiveV1Data:
    sender: EventSender | None
    message: EventMessage | None
    def __init__(self, d=None) -> None: ...

class P2ImMessageReceiveV1(EventContext):
    event: P2ImMessageReceiveV1Data | None
    def __init__(self, d=None) -> None: ...
