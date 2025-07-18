from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrPersonUpdatedV1Data:
    person_id: str | None
    field_changes: list[str] | None
    def __init__(self, d=None) -> None: ...

class P2CorehrPersonUpdatedV1(EventContext):
    event: P2CorehrPersonUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
