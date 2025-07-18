from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HelpdeskNotificationApproveV1Data:
    notification_id: str | None
    helpdesk_id: str | None
    approve_status: str | None
    def __init__(self, d=None) -> None: ...

class P2HelpdeskNotificationApproveV1(EventContext):
    event: P2HelpdeskNotificationApproveV1Data | None
    def __init__(self, d=None) -> None: ...
