from lark_oapi.core.construct import init as init

class OrderCondition:
    field: str | None
    order_type: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OrderConditionBuilder: ...

class OrderConditionBuilder:
    def __init__(self) -> None: ...
    def field(self, field: str) -> OrderConditionBuilder: ...
    def order_type(self, order_type: str) -> OrderConditionBuilder: ...
    def build(self) -> OrderCondition: ...
