from lark_oapi.core.construct import init as init

class DeleteFaqResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteFaqResponseBodyBuilder: ...

class DeleteFaqResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DeleteFaqResponseBody: ...
