from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrDepartmentDeletedV1Data:
    department_id: str | None
    code: str | None
    def __init__(self, d=None) -> None: ...

class P2CorehrDepartmentDeletedV1(EventContext):
    event: P2CorehrDepartmentDeletedV1Data | None
    def __init__(self, d=None) -> None: ...
