from .emoji import Emoji as Emoji
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ImMessageReactionDeletedV1Data:
    message_id: str | None
    reaction_type: Emoji | None
    operator_type: str | None
    user_id: UserId | None
    app_id: str | None
    action_time: str | None
    def __init__(self, d=None) -> None: ...

class P2ImMessageReactionDeletedV1(EventContext):
    event: P2ImMessageReactionDeletedV1Data | None
    def __init__(self, d=None) -> None: ...
