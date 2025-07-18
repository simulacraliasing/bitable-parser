from lark_oapi.core.construct import init as init

class OpeningTimePeriodExternal:
    start_hhmm: int | None
    end_hhmm: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OpeningTimePeriodExternalBuilder: ...

class OpeningTimePeriodExternalBuilder:
    def __init__(self) -> None: ...
    def start_hhmm(self, start_hhmm: int) -> OpeningTimePeriodExternalBuilder: ...
    def end_hhmm(self, end_hhmm: int) -> OpeningTimePeriodExternalBuilder: ...
    def build(self) -> OpeningTimePeriodExternal: ...
