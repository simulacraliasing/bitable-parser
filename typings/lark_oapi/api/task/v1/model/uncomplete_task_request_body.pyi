from lark_oapi.core.construct import init as init

class UncompleteTaskRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UncompleteTaskRequestBodyBuilder: ...

class UncompleteTaskRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> UncompleteTaskRequestBody: ...
