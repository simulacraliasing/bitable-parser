from lark_oapi.core.construct import init as init

class ActiveLocationResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ActiveLocationResponseBodyBuilder: ...

class ActiveLocationResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> ActiveLocationResponseBody: ...
