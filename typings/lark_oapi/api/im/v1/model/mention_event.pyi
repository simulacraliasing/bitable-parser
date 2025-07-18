from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init

class MentionEvent:
    key: str | None
    id: UserId | None
    name: str | None
    tenant_key: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MentionEventBuilder: ...

class MentionEventBuilder:
    def __init__(self) -> None: ...
    def key(self, key: str) -> MentionEventBuilder: ...
    def id(self, id: UserId) -> MentionEventBuilder: ...
    def name(self, name: str) -> MentionEventBuilder: ...
    def tenant_key(self, tenant_key: str) -> MentionEventBuilder: ...
    def build(self) -> MentionEvent: ...
