from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ApplicationApplicationFeedbackUpdatedV6Data:
    feedback_ids: list[str] | None
    status: int | None
    app_id: str | None
    update_time: str | None
    operator_id: UserId | None
    def __init__(self, d=None) -> None: ...

class P2ApplicationApplicationFeedbackUpdatedV6(EventContext):
    event: P2ApplicationApplicationFeedbackUpdatedV6Data | None
    def __init__(self, d=None) -> None: ...
