from .i18n_names import I18nNames as I18nNames
from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2ImChatMemberBotAddedV1Data:
    chat_id: str | None
    operator_id: UserId | None
    external: bool | None
    operator_tenant_key: str | None
    name: str | None
    i18n_names: I18nNames | None
    def __init__(self, d=None) -> None: ...

class P2ImChatMemberBotAddedV1(EventContext):
    event: P2ImChatMemberBotAddedV1Data | None
    def __init__(self, d=None) -> None: ...
