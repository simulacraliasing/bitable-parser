from lark_oapi.core.construct import init as init

class CreateAppAccessTokenResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateAppAccessTokenResponseBodyBuilder: ...

class CreateAppAccessTokenResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> CreateAppAccessTokenResponseBody: ...
