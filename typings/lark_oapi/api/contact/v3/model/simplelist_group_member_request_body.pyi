from lark_oapi.core.construct import init as init

class SimplelistGroupMemberRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SimplelistGroupMemberRequestBodyBuilder: ...

class SimplelistGroupMemberRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> SimplelistGroupMemberRequestBody: ...
