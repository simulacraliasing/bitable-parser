from lark_oapi.core.construct import init as init

class CreatePeriodResponseBody:
    period_id: str | None
    start_month: str | None
    end_month: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreatePeriodResponseBodyBuilder: ...

class CreatePeriodResponseBodyBuilder:
    def __init__(self) -> None: ...
    def period_id(self, period_id: str) -> CreatePeriodResponseBodyBuilder: ...
    def start_month(self, start_month: str) -> CreatePeriodResponseBodyBuilder: ...
    def end_month(self, end_month: str) -> CreatePeriodResponseBodyBuilder: ...
    def build(self) -> CreatePeriodResponseBody: ...
