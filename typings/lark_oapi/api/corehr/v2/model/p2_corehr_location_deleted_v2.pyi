from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrLocationDeletedV2Data:
    location_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrLocationDeletedV2(EventContext):
    event: P2CorehrLocationDeletedV2Data | None
    def __init__(self, d=None) -> None: ...
