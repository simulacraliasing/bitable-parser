from lark_oapi.core.construct import init as init

class IdConvertCardResponseBody:
    card_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> IdConvertCardResponseBodyBuilder: ...

class IdConvertCardResponseBodyBuilder:
    def __init__(self) -> None: ...
    def card_id(self, card_id: str) -> IdConvertCardResponseBodyBuilder: ...
    def build(self) -> IdConvertCardResponseBody: ...
