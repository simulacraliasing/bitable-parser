from lark_oapi.core.construct import init as init

class ListEntityRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListEntityRequestBodyBuilder: ...

class ListEntityRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListEntityRequestBody: ...
