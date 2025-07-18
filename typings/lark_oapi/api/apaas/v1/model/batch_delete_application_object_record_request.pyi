from .batch_delete_application_object_record_request_body import BatchDeleteApplicationObjectRecordRequestBody as BatchDeleteApplicationObjectRecordRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class BatchDeleteApplicationObjectRecordRequest(BaseRequest):
    namespace: str | None
    object_api_name: str | None
    request_body: BatchDeleteApplicationObjectRecordRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> BatchDeleteApplicationObjectRecordRequestBuilder: ...

class BatchDeleteApplicationObjectRecordRequestBuilder:
    def __init__(self) -> None: ...
    def namespace(self, namespace: str) -> BatchDeleteApplicationObjectRecordRequestBuilder: ...
    def object_api_name(self, object_api_name: str) -> BatchDeleteApplicationObjectRecordRequestBuilder: ...
    def request_body(self, request_body: BatchDeleteApplicationObjectRecordRequestBody) -> BatchDeleteApplicationObjectRecordRequestBuilder: ...
    def build(self) -> BatchDeleteApplicationObjectRecordRequest: ...
