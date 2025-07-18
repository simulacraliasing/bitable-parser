from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ApplicationApplicationAppVersionPublishRevokeV6Data:
    operator_id: UserId | None
    creator_id: UserId | None
    app_id: str | None
    version_id: str | None
    def __init__(self, d=None) -> None: ...

class P2ApplicationApplicationAppVersionPublishRevokeV6(EventContext):
    event: P2ApplicationApplicationAppVersionPublishRevokeV6Data | None
    def __init__(self, d=None) -> None: ...
