from lark_oapi.core.construct import init as init

class UnsubscribeEventResponseBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UnsubscribeEventResponseBodyBuilder: ...

class UnsubscribeEventResponseBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> UnsubscribeEventResponseBody: ...
