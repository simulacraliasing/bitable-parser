from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ImMessageRecalledV1Data:
    message_id: str | None
    chat_id: str | None
    recall_time: str | None
    recall_type: str | None
    def __init__(self, d=None) -> None: ...

class P2ImMessageRecalledV1(EventContext):
    event: P2ImMessageRecalledV1Data | None
    def __init__(self, d=None) -> None: ...
