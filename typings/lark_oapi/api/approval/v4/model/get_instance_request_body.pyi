from lark_oapi.core.construct import init as init

class GetInstanceRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetInstanceRequestBodyBuilder: ...

class GetInstanceRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> GetInstanceRequestBody: ...
