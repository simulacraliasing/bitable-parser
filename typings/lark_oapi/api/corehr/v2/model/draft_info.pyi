from lark_oapi.core.construct import init as init

class DraftInfo:
    draft_id: str | None
    topic: str | None
    adjust_reason: str | None
    effective_date: str | None
    department_adjust_record_ids: list[str] | None
    job_change_adjust_record_ids: list[str] | None
    position_adjust_record_ids: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DraftInfoBuilder: ...

class DraftInfoBuilder:
    def __init__(self) -> None: ...
    def draft_id(self, draft_id: str) -> DraftInfoBuilder: ...
    def topic(self, topic: str) -> DraftInfoBuilder: ...
    def adjust_reason(self, adjust_reason: str) -> DraftInfoBuilder: ...
    def effective_date(self, effective_date: str) -> DraftInfoBuilder: ...
    def department_adjust_record_ids(self, department_adjust_record_ids: list[str]) -> DraftInfoBuilder: ...
    def job_change_adjust_record_ids(self, job_change_adjust_record_ids: list[str]) -> DraftInfoBuilder: ...
    def position_adjust_record_ids(self, position_adjust_record_ids: list[str]) -> DraftInfoBuilder: ...
    def build(self) -> DraftInfo: ...
