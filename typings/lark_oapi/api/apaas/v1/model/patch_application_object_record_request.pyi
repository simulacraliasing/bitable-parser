from .patch_application_object_record_request_body import PatchApplicationObjectRecordRequestBody as PatchApplicationObjectRecordRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchApplicationObjectRecordRequest(BaseRequest):
    namespace: str | None
    object_api_name: str | None
    id: str | None
    request_body: PatchApplicationObjectRecordRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchApplicationObjectRecordRequestBuilder: ...

class PatchApplicationObjectRecordRequestBuilder:
    def __init__(self) -> None: ...
    def namespace(self, namespace: str) -> PatchApplicationObjectRecordRequestBuilder: ...
    def object_api_name(self, object_api_name: str) -> PatchApplicationObjectRecordRequestBuilder: ...
    def id(self, id: str) -> PatchApplicationObjectRecordRequestBuilder: ...
    def request_body(self, request_body: PatchApplicationObjectRecordRequestBody) -> PatchApplicationObjectRecordRequestBuilder: ...
    def build(self) -> PatchApplicationObjectRecordRequest: ...
