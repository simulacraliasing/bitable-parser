from lark_oapi.core.construct import init as init

class CreateScopeConfigResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateScopeConfigResponseBodyBuilder: ...

class CreateScopeConfigResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> CreateScopeConfigResponseBody: ...
