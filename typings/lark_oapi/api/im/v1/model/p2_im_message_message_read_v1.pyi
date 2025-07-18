from .event_message_reader import EventMessageReader as EventMessageReader
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ImMessageMessageReadV1Data:
    reader: EventMessageReader | None
    message_id_list: list[str] | None
    def __init__(self, d=None) -> None: ...

class P2ImMessageMessageReadV1(EventContext):
    event: P2ImMessageMessageReadV1Data | None
    def __init__(self, d=None) -> None: ...
