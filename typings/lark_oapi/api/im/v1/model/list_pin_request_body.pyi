from lark_oapi.core.construct import init as init

class ListPinRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListPinRequestBodyBuilder: ...

class ListPinRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListPinRequestBody: ...
