from lark_oapi.core.construct import init as init

class PatchCardElementResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PatchCardElementResponseBodyBuilder: ...

class PatchCardElementResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> PatchCardElementResponseBody: ...
