from lark_oapi.core.construct import init as init

class GetAppRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetAppRequestBodyBuilder: ...

class GetAppRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> GetAppRequestBody: ...
