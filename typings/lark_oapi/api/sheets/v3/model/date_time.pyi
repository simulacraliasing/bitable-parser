from lark_oapi.core.construct import init as init

class DateTime:
    date_time: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DateTimeBuilder: ...

class DateTimeBuilder:
    def __init__(self) -> None: ...
    def date_time(self, date_time: str) -> DateTimeBuilder: ...
    def build(self) -> DateTime: ...
