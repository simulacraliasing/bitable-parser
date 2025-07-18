from .batch_create_app_table_record_request_body import BatchCreateAppTableRecordRequestBody as BatchCreateAppTableRecordRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class BatchCreateAppTableRecordRequest(BaseRequest):
    user_id_type: str | None
    client_token: str | None
    ignore_consistency_check: bool | None
    app_token: str | None
    table_id: str | None
    request_body: BatchCreateAppTableRecordRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> BatchCreateAppTableRecordRequestBuilder: ...

class BatchCreateAppTableRecordRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> BatchCreateAppTableRecordRequestBuilder: ...
    def client_token(self, client_token: str) -> BatchCreateAppTableRecordRequestBuilder: ...
    def ignore_consistency_check(self, ignore_consistency_check: bool) -> BatchCreateAppTableRecordRequestBuilder: ...
    def app_token(self, app_token: str) -> BatchCreateAppTableRecordRequestBuilder: ...
    def table_id(self, table_id: str) -> BatchCreateAppTableRecordRequestBuilder: ...
    def request_body(self, request_body: BatchCreateAppTableRecordRequestBody) -> BatchCreateAppTableRecordRequestBuilder: ...
    def build(self) -> BatchCreateAppTableRecordRequest: ...
