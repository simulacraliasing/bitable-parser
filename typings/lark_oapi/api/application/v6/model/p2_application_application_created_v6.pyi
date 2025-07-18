from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ApplicationApplicationCreatedV6Data:
    operator_id: UserId | None
    app_id: str | None
    name: str | None
    description: str | None
    avatar: str | None
    app_scene_type: int | None
    primary_language: str | None
    create_source: str | None
    def __init__(self, d=None) -> None: ...

class P2ApplicationApplicationCreatedV6(EventContext):
    event: P2ApplicationApplicationCreatedV6Data | None
    def __init__(self, d=None) -> None: ...
