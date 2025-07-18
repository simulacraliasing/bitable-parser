from lark_oapi.core.construct import init as init

class ProgressRate:
    percent: int | None
    status: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ProgressRateBuilder: ...

class ProgressRateBuilder:
    def __init__(self) -> None: ...
    def percent(self, percent: int) -> ProgressRateBuilder: ...
    def status(self, status: int) -> ProgressRateBuilder: ...
    def build(self) -> ProgressRate: ...
