from lark_oapi.core.construct import init as init

class DeleteManagersChatManagersResponseBody:
    chat_managers: list[str] | None
    chat_bot_managers: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteManagersChatManagersResponseBodyBuilder: ...

class DeleteManagersChatManagersResponseBodyBuilder:
    def __init__(self) -> None: ...
    def chat_managers(self, chat_managers: list[str]) -> DeleteManagersChatManagersResponseBodyBuilder: ...
    def chat_bot_managers(self, chat_bot_managers: list[str]) -> DeleteManagersChatManagersResponseBodyBuilder: ...
    def build(self) -> DeleteManagersChatManagersResponseBody: ...
