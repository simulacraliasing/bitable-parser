from lark_oapi.core.construct import init as init

class GetFaqRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetFaqRequestBodyBuilder: ...

class GetFaqRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> GetFaqRequestBody: ...
