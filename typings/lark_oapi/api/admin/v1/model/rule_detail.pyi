from lark_oapi.core.construct import init as init

class RuleDetail:
    effective_time: int | None
    expiration_time: int | None
    anniversary: int | None
    effective_period: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> RuleDetailBuilder: ...

class RuleDetailBuilder:
    def __init__(self) -> None: ...
    def effective_time(self, effective_time: int) -> RuleDetailBuilder: ...
    def expiration_time(self, expiration_time: int) -> RuleDetailBuilder: ...
    def anniversary(self, anniversary: int) -> RuleDetailBuilder: ...
    def effective_period(self, effective_period: int) -> RuleDetailBuilder: ...
    def build(self) -> RuleDetail: ...
