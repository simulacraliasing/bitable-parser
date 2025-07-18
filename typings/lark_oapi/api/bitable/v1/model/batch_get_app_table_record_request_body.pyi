from lark_oapi.core.construct import init as init

class BatchGetAppTableRecordRequestBody:
    record_ids: list[str] | None
    user_id_type: str | None
    with_shared_url: bool | None
    automatic_fields: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchGetAppTableRecordRequestBodyBuilder: ...

class BatchGetAppTableRecordRequestBodyBuilder:
    def __init__(self) -> None: ...
    def record_ids(self, record_ids: list[str]) -> BatchGetAppTableRecordRequestBodyBuilder: ...
    def user_id_type(self, user_id_type: str) -> BatchGetAppTableRecordRequestBodyBuilder: ...
    def with_shared_url(self, with_shared_url: bool) -> BatchGetAppTableRecordRequestBodyBuilder: ...
    def automatic_fields(self, automatic_fields: bool) -> BatchGetAppTableRecordRequestBodyBuilder: ...
    def build(self) -> BatchGetAppTableRecordRequestBody: ...
