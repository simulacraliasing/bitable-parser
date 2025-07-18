from .due import Due as Due
from .member import Member as Member
from .start import Start as Start
from lark_oapi.core.construct import init as init

class TaskSummary:
    guid: str | None
    summary: str | None
    completed_at: int | None
    start: Start | None
    due: Due | None
    members: list[Member] | None
    subtask_count: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TaskSummaryBuilder: ...

class TaskSummaryBuilder:
    def __init__(self) -> None: ...
    def guid(self, guid: str) -> TaskSummaryBuilder: ...
    def summary(self, summary: str) -> TaskSummaryBuilder: ...
    def completed_at(self, completed_at: int) -> TaskSummaryBuilder: ...
    def start(self, start: Start) -> TaskSummaryBuilder: ...
    def due(self, due: Due) -> TaskSummaryBuilder: ...
    def members(self, members: list[Member]) -> TaskSummaryBuilder: ...
    def subtask_count(self, subtask_count: int) -> TaskSummaryBuilder: ...
    def build(self) -> TaskSummary: ...
