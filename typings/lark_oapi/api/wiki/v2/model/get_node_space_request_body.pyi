from lark_oapi.core.construct import init as init

class GetNodeSpaceRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetNodeSpaceRequestBodyBuilder: ...

class GetNodeSpaceRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> GetNodeSpaceRequestBody: ...
