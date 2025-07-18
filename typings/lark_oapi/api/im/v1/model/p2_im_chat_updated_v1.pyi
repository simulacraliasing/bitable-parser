from .chat_change import ChatChange as ChatChange
from .moderator_list import ModeratorList as ModeratorList
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ImChatUpdatedV1Data:
    chat_id: str | None
    operator_id: UserId | None
    external: bool | None
    operator_tenant_key: str | None
    after_change: ChatChange | None
    before_change: ChatChange | None
    moderator_list: ModeratorList | None
    def __init__(self, d=None) -> None: ...

class P2ImChatUpdatedV1(EventContext):
    event: P2ImChatUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
