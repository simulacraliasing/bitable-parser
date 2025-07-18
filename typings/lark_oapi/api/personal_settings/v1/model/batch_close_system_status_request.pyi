from .batch_close_system_status_request_body import BatchCloseSystemStatusRequestBody as BatchCloseSystemStatusRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class BatchCloseSystemStatusRequest(BaseRequest):
    user_id_type: str | None
    system_status_id: int | None
    request_body: BatchCloseSystemStatusRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> BatchCloseSystemStatusRequestBuilder: ...

class BatchCloseSystemStatusRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> BatchCloseSystemStatusRequestBuilder: ...
    def system_status_id(self, system_status_id: int) -> BatchCloseSystemStatusRequestBuilder: ...
    def request_body(self, request_body: BatchCloseSystemStatusRequestBody) -> BatchCloseSystemStatusRequestBuilder: ...
    def build(self) -> BatchCloseSystemStatusRequest: ...
