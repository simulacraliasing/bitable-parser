from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ApplicationApplicationAppVersionAuditV6Data:
    operator_id: UserId | None
    version_id: str | None
    creator_id: UserId | None
    app_id: str | None
    operation: str | None
    remark: str | None
    audit_source: str | None
    def __init__(self, d=None) -> None: ...

class P2ApplicationApplicationAppVersionAuditV6(EventContext):
    event: P2ApplicationApplicationAppVersionAuditV6Data | None
    def __init__(self, d=None) -> None: ...
