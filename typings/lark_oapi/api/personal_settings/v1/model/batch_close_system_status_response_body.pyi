from .system_status_user_close_result_entity import SystemStatusUserCloseResultEntity as SystemStatusUserCloseResultEntity
from lark_oapi.core.construct import init as init

class BatchCloseSystemStatusResponseBody:
    result_list: list[SystemStatusUserCloseResultEntity] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchCloseSystemStatusResponseBodyBuilder: ...

class BatchCloseSystemStatusResponseBodyBuilder:
    def __init__(self) -> None: ...
    def result_list(self, result_list: list[SystemStatusUserCloseResultEntity]) -> BatchCloseSystemStatusResponseBodyBuilder: ...
    def build(self) -> BatchCloseSystemStatusResponseBody: ...
