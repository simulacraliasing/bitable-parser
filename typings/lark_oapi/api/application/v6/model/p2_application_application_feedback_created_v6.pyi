from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ApplicationApplicationFeedbackCreatedV6Data:
    user_id: UserId | None
    app_id: str | None
    feedback_time: str | None
    tenant_name: str | None
    feedback_type: int | None
    fault_type: list[int] | None
    fault_time: str | None
    source: int | None
    contact: str | None
    description: str | None
    images: list[str] | None
    feedback_id: str | None
    feedback_path: str | None
    def __init__(self, d=None) -> None: ...

class P2ApplicationApplicationFeedbackCreatedV6(EventContext):
    event: P2ApplicationApplicationFeedbackCreatedV6Data | None
    def __init__(self, d=None) -> None: ...
