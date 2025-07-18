from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2TaskTaskUpdatedV1Data:
    task_id: str | None
    obj_type: int | None
    def __init__(self, d=None) -> None: ...

class P2TaskTaskUpdatedV1(EventContext):
    event: P2TaskTaskUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
