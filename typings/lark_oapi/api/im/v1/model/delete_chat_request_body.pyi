from lark_oapi.core.construct import init as init

class DeleteChatRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteChatRequestBodyBuilder: ...

class DeleteChatRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteChatRequestBody: ...
