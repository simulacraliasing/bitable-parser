from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireTalentDeletedV1Data:
    talent_id: str | None
    def __init__(self, d=None) -> None: ...

class P2HireTalentDeletedV1(EventContext):
    event: P2HireTalentDeletedV1Data | None
    def __init__(self, d=None) -> None: ...
