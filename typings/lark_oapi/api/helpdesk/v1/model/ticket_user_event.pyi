from .user_id import UserId as UserId
from lark_oapi.core.construct import init as init

class TicketUserEvent:
    id: UserId | None
    avatar_url: str | None
    name: str | None
    email: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TicketUserEventBuilder: ...

class TicketUserEventBuilder:
    def __init__(self) -> None: ...
    def id(self, id: UserId) -> TicketUserEventBuilder: ...
    def avatar_url(self, avatar_url: str) -> TicketUserEventBuilder: ...
    def name(self, name: str) -> TicketUserEventBuilder: ...
    def email(self, email: str) -> TicketUserEventBuilder: ...
    def build(self) -> TicketUserEvent: ...
