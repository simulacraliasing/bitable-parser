from lark_oapi.core.construct import init as init

class IsInChatChatMembersResponseBody:
    is_in_chat: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> IsInChatChatMembersResponseBodyBuilder: ...

class IsInChatChatMembersResponseBodyBuilder:
    def __init__(self) -> None: ...
    def is_in_chat(self, is_in_chat: bool) -> IsInChatChatMembersResponseBodyBuilder: ...
    def build(self) -> IsInChatChatMembersResponseBody: ...
