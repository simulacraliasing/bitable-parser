from lark_oapi.core.construct import init as init

class OvertimeClockCfg:
    allow_punch_approval: bool | None
    need_clock_over_time_start_and_end: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OvertimeClockCfgBuilder: ...

class OvertimeClockCfgBuilder:
    def __init__(self) -> None: ...
    def allow_punch_approval(self, allow_punch_approval: bool) -> OvertimeClockCfgBuilder: ...
    def need_clock_over_time_start_and_end(self, need_clock_over_time_start_and_end: bool) -> OvertimeClockCfgBuilder: ...
    def build(self) -> OvertimeClockCfg: ...
