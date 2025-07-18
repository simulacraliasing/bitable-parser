from lark_oapi.core.construct import init as init

class CreateInstanceResponseBody:
    instance_code: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateInstanceResponseBodyBuilder: ...

class CreateInstanceResponseBodyBuilder:
    def __init__(self) -> None: ...
    def instance_code(self, instance_code: str) -> CreateInstanceResponseBodyBuilder: ...
    def build(self) -> CreateInstanceResponseBody: ...
