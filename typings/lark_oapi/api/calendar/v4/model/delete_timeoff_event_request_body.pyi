from lark_oapi.core.construct import init as init

class DeleteTimeoffEventRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteTimeoffEventRequestBodyBuilder: ...

class DeleteTimeoffEventRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteTimeoffEventRequestBody: ...
