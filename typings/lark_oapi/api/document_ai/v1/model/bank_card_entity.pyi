from lark_oapi.core.construct import init as init

class BankCardEntity:
    type: str | None
    value: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BankCardEntityBuilder: ...

class BankCardEntityBuilder:
    def __init__(self) -> None: ...
    def type(self, type: str) -> BankCardEntityBuilder: ...
    def value(self, value: str) -> BankCardEntityBuilder: ...
    def build(self) -> BankCardEntity: ...
