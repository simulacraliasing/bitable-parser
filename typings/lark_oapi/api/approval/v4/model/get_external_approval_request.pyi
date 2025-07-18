from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetExternalApprovalRequest(BaseRequest):
    user_id_type: str | None
    approval_code: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetExternalApprovalRequestBuilder: ...

class GetExternalApprovalRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> GetExternalApprovalRequestBuilder: ...
    def approval_code(self, approval_code: str) -> GetExternalApprovalRequestBuilder: ...
    def build(self) -> GetExternalApprovalRequest: ...
