from .chat_tab import ChatTab as ChatTab
from lark_oapi.core.construct import init as init

class CreateChatTabRequestBody:
    chat_tabs: list[ChatTab] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateChatTabRequestBodyBuilder: ...

class CreateChatTabRequestBodyBuilder:
    def __init__(self) -> None: ...
    def chat_tabs(self, chat_tabs: list[ChatTab]) -> CreateChatTabRequestBodyBuilder: ...
    def build(self) -> CreateChatTabRequestBody: ...
