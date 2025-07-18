from .record_result import RecordResult as RecordResult
from lark_oapi.core.construct import init as init

class BatchUpdateApplicationObjectRecordResponseBody:
    items: list[RecordResult] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchUpdateApplicationObjectRecordResponseBodyBuilder: ...

class BatchUpdateApplicationObjectRecordResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[RecordResult]) -> BatchUpdateApplicationObjectRecordResponseBodyBuilder: ...
    def build(self) -> BatchUpdateApplicationObjectRecordResponseBody: ...
