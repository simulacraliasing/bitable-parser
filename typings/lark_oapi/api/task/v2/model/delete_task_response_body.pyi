from lark_oapi.core.construct import init as init

class DeleteTaskResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteTaskResponseBodyBuilder: ...

class DeleteTaskResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteTaskResponseBody: ...
