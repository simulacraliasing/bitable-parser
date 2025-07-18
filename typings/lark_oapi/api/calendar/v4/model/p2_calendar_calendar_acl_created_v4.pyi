from .acl_scope_event import AclScopeEvent as AclScopeEvent
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CalendarCalendarAclCreatedV4Data:
    acl_id: str | None
    role: str | None
    scope: AclScopeEvent | None
    user_id_list: list[UserId] | None
    def __init__(self, d=None) -> None: ...

class P2CalendarCalendarAclCreatedV4(EventContext):
    event: P2CalendarCalendarAclCreatedV4Data | None
    def __init__(self, d=None) -> None: ...
