from lark_oapi.core.construct import init as init

class DeleteShiftResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteShiftResponseBodyBuilder: ...

class DeleteShiftResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteShiftResponseBody: ...
