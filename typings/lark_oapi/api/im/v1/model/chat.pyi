from .i18n_names import I18nNames as I18nNames
from lark_oapi.core.construct import init as init

class Chat:
    chat_id: str | None
    avatar: str | None
    name: str | None
    description: str | None
    i18n_names: I18nNames | None
    only_owner_add: bool | None
    share_allowed: bool | None
    only_owner_at_all: bool | None
    only_owner_edit: bool | None
    owner_user_id: str | None
    type: str | None
    labels: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ChatBuilder: ...

class ChatBuilder:
    def __init__(self) -> None: ...
    def chat_id(self, chat_id: str) -> ChatBuilder: ...
    def avatar(self, avatar: str) -> ChatBuilder: ...
    def name(self, name: str) -> ChatBuilder: ...
    def description(self, description: str) -> ChatBuilder: ...
    def i18n_names(self, i18n_names: I18nNames) -> ChatBuilder: ...
    def only_owner_add(self, only_owner_add: bool) -> ChatBuilder: ...
    def share_allowed(self, share_allowed: bool) -> ChatBuilder: ...
    def only_owner_at_all(self, only_owner_at_all: bool) -> ChatBuilder: ...
    def only_owner_edit(self, only_owner_edit: bool) -> ChatBuilder: ...
    def owner_user_id(self, owner_user_id: str) -> ChatBuilder: ...
    def type(self, type: str) -> ChatBuilder: ...
    def labels(self, labels: list[str]) -> ChatBuilder: ...
    def build(self) -> Chat: ...
