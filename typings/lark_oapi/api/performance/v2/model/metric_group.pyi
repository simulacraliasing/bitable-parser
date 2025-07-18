from lark_oapi.core.construct import init as init

class MetricGroup:
    group_id: int | None
    name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MetricGroupBuilder: ...

class MetricGroupBuilder:
    def __init__(self) -> None: ...
    def group_id(self, group_id: int) -> MetricGroupBuilder: ...
    def name(self, name: str) -> MetricGroupBuilder: ...
    def build(self) -> MetricGroup: ...
