from lark_oapi.core.construct import init as init

class ChatMembers:
    user_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ChatMembersBuilder: ...

class ChatMembersBuilder:
    def __init__(self) -> None: ...
    def user_id(self, user_id: str) -> ChatMembersBuilder: ...
    def build(self) -> ChatMembers: ...
