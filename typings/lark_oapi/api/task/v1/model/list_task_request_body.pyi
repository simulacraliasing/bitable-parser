from lark_oapi.core.construct import init as init

class ListTaskRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListTaskRequestBodyBuilder: ...

class ListTaskRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListTaskRequestBody: ...
