from .application_app_version_event import ApplicationAppVersionEvent as ApplicationAppVersionEvent
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ApplicationApplicationAppVersionPublishApplyV6Data:
    operator_id: UserId | None
    online_version: ApplicationAppVersionEvent | None
    under_audit_version: ApplicationAppVersionEvent | None
    app_status: int | None
    def __init__(self, d=None) -> None: ...

class P2ApplicationApplicationAppVersionPublishApplyV6(EventContext):
    event: P2ApplicationApplicationAppVersionPublishApplyV6Data | None
    def __init__(self, d=None) -> None: ...
