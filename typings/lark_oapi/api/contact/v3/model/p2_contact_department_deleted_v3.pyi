from .department_event import DepartmentEvent as DepartmentEvent
from .old_department_object import OldDepartmentObject as OldDepartmentObject
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ContactDepartmentDeletedV3Data:
    object: DepartmentEvent | None
    old_object: OldDepartmentObject | None
    def __init__(self, d=None) -> None: ...

class P2ContactDepartmentDeletedV3(EventContext):
    event: P2ContactDepartmentDeletedV3Data | None
    def __init__(self, d=None) -> None: ...
