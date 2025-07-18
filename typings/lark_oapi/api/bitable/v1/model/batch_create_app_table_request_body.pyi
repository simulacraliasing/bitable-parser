from .req_table import ReqTable as ReqTable
from lark_oapi.core.construct import init as init

class BatchCreateAppTableRequestBody:
    tables: list[ReqTable] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchCreateAppTableRequestBodyBuilder: ...

class BatchCreateAppTableRequestBodyBuilder:
    def __init__(self) -> None: ...
    def tables(self, tables: list[ReqTable]) -> BatchCreateAppTableRequestBodyBuilder: ...
    def build(self) -> BatchCreateAppTableRequestBody: ...
