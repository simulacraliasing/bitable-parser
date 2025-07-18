from .department_event import DepartmentEvent as DepartmentEvent
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ContactDepartmentCreatedV3Data:
    object: DepartmentEvent | None
    def __init__(self, d=None) -> None: ...

class P2ContactDepartmentCreatedV3(EventContext):
    event: P2ContactDepartmentCreatedV3Data | None
    def __init__(self, d=None) -> None: ...
