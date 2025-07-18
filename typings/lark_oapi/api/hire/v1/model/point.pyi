from lark_oapi.core.construct import init as init

class Point:
    amount: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PointBuilder: ...

class PointBuilder:
    def __init__(self) -> None: ...
    def amount(self, amount: int) -> PointBuilder: ...
    def build(self) -> Point: ...
