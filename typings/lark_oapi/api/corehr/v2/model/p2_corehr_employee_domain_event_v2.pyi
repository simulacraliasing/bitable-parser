from .employee_domain_event_data import EmployeeDomainEventData as EmployeeDomainEventData
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrEmployeeDomainEventV2Data:
    event_type: int | None
    sub_event_type: int | None
    operator_user_id: str | None
    opt_scene: str | None
    opt_desc: str | None
    opt_time: str | None
    opt_id: str | None
    employment_id: str | None
    data: list[EmployeeDomainEventData] | None
    def __init__(self, d=None) -> None: ...

class P2CorehrEmployeeDomainEventV2(EventContext):
    event: P2CorehrEmployeeDomainEventV2Data | None
    def __init__(self, d=None) -> None: ...
