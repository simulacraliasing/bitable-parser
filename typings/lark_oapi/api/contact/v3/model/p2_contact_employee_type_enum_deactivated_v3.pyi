from .employee_type_enum import EmployeeTypeEnum as EmployeeTypeEnum
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ContactEmployeeTypeEnumDeactivatedV3Data:
    old_enum: EmployeeTypeEnum | None
    new_enum: EmployeeTypeEnum | None
    def __init__(self, d=None) -> None: ...

class P2ContactEmployeeTypeEnumDeactivatedV3(EventContext):
    event: P2ContactEmployeeTypeEnumDeactivatedV3Data | None
    def __init__(self, d=None) -> None: ...
