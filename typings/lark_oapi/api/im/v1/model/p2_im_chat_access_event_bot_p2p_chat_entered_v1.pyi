from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ImChatAccessEventBotP2pChatEnteredV1Data:
    chat_id: str | None
    operator_id: UserId | None
    last_message_id: str | None
    last_message_create_time: str | None
    def __init__(self, d=None) -> None: ...

class P2ImChatAccessEventBotP2pChatEnteredV1(EventContext):
    event: P2ImChatAccessEventBotP2pChatEnteredV1Data | None
    def __init__(self, d=None) -> None: ...
