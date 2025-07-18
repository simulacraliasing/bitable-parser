from .batch_create_mailgroup_manager_request_body import BatchCreateMailgroupManagerRequestBody as BatchCreateMailgroupManagerRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class BatchCreateMailgroupManagerRequest(BaseRequest):
    user_id_type: str | None
    mailgroup_id: str | None
    request_body: BatchCreateMailgroupManagerRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> BatchCreateMailgroupManagerRequestBuilder: ...

class BatchCreateMailgroupManagerRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> BatchCreateMailgroupManagerRequestBuilder: ...
    def mailgroup_id(self, mailgroup_id: str) -> BatchCreateMailgroupManagerRequestBuilder: ...
    def request_body(self, request_body: BatchCreateMailgroupManagerRequestBody) -> BatchCreateMailgroupManagerRequestBuilder: ...
    def build(self) -> BatchCreateMailgroupManagerRequest: ...
