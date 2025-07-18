from .chat_menu_tree import ChatMenuTree as ChatMenuTree
from lark_oapi.core.construct import init as init

class CreateChatMenuTreeRequestBody:
    menu_tree: ChatMenuTree | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateChatMenuTreeRequestBodyBuilder: ...

class CreateChatMenuTreeRequestBodyBuilder:
    def __init__(self) -> None: ...
    def menu_tree(self, menu_tree: ChatMenuTree) -> CreateChatMenuTreeRequestBodyBuilder: ...
    def build(self) -> CreateChatMenuTreeRequestBody: ...
