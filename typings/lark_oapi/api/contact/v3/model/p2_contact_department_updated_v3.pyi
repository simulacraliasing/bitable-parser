from .department_event import DepartmentEvent as DepartmentEvent
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ContactDepartmentUpdatedV3Data:
    object: DepartmentEvent | None
    old_object: DepartmentEvent | None
    def __init__(self, d=None) -> None: ...

class P2ContactDepartmentUpdatedV3(EventContext):
    event: P2ContactDepartmentUpdatedV3Data | None
    def __init__(self, d=None) -> None: ...
