from lark_oapi.core.construct import init as init

class ListSecurityGroupRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListSecurityGroupRequestBodyBuilder: ...

class ListSecurityGroupRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ListSecurityGroupRequestBody: ...
