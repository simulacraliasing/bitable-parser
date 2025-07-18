from .job_level import JobLevel as JobLevel
from lark_oapi.core.construct import init as init

class BatchGetJobLevelResponseBody:
    items: list[JobLevel] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchGetJobLevelResponseBodyBuilder: ...

class BatchGetJobLevelResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[JobLevel]) -> BatchGetJobLevelResponseBodyBuilder: ...
    def build(self) -> BatchGetJobLevelResponseBody: ...
