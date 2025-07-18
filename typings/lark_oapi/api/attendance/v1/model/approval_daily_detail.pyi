from lark_oapi.core.construct import init as init

class ApprovalDailyDetail:
    date: str | None
    duration: str | None
    overtime_unit: int | None
    overtime_date_type: int | None
    settle_type_enum: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ApprovalDailyDetailBuilder: ...

class ApprovalDailyDetailBuilder:
    def __init__(self) -> None: ...
    def date(self, date: str) -> ApprovalDailyDetailBuilder: ...
    def duration(self, duration: str) -> ApprovalDailyDetailBuilder: ...
    def overtime_unit(self, overtime_unit: int) -> ApprovalDailyDetailBuilder: ...
    def overtime_date_type(self, overtime_date_type: int) -> ApprovalDailyDetailBuilder: ...
    def settle_type_enum(self, settle_type_enum: int) -> ApprovalDailyDetailBuilder: ...
    def build(self) -> ApprovalDailyDetail: ...
