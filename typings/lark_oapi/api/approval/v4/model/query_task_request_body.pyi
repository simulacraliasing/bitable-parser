from lark_oapi.core.construct import init as init

class QueryTaskRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryTaskRequestBodyBuilder: ...

class QueryTaskRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> QueryTaskRequestBody: ...
