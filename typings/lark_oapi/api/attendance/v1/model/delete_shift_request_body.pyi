from lark_oapi.core.construct import init as init

class DeleteShiftRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteShiftRequestBodyBuilder: ...

class DeleteShiftRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteShiftRequestBody: ...
