from .app_table_record import AppTableRecord as AppTableRecord
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UpdateAppTableRecordRequest(BaseRequest):
    user_id_type: str | None
    ignore_consistency_check: bool | None
    app_token: str | None
    table_id: str | None
    record_id: str | None
    request_body: AppTableRecord | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UpdateAppTableRecordRequestBuilder: ...

class UpdateAppTableRecordRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> UpdateAppTableRecordRequestBuilder: ...
    def ignore_consistency_check(self, ignore_consistency_check: bool) -> UpdateAppTableRecordRequestBuilder: ...
    def app_token(self, app_token: str) -> UpdateAppTableRecordRequestBuilder: ...
    def table_id(self, table_id: str) -> UpdateAppTableRecordRequestBuilder: ...
    def record_id(self, record_id: str) -> UpdateAppTableRecordRequestBuilder: ...
    def request_body(self, request_body: AppTableRecord) -> UpdateAppTableRecordRequestBuilder: ...
    def build(self) -> UpdateAppTableRecordRequest: ...
