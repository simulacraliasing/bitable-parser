from lark_oapi.core.construct import init as init

class ReadUsersMessageRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ReadUsersMessageRequestBodyBuilder: ...

class ReadUsersMessageRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ReadUsersMessageRequestBody: ...
