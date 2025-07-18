from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireApplicationDeletedV1Data:
    application_ids: list[str] | None
    def __init__(self, d=None) -> None: ...

class P2HireApplicationDeletedV1(EventContext):
    event: P2HireApplicationDeletedV1Data | None
    def __init__(self, d=None) -> None: ...
