from lark_oapi.core.construct import init as init

class CompleteTaskRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CompleteTaskRequestBodyBuilder: ...

class CompleteTaskRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> CompleteTaskRequestBody: ...
