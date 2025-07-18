from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrDepartmentCreatedV2Data:
    department_id: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrDepartmentCreatedV2(EventContext):
    event: P2CorehrDepartmentCreatedV2Data | None
    def __init__(self, d=None) -> None: ...
