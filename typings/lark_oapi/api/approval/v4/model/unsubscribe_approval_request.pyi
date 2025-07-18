from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UnsubscribeApprovalRequest(BaseRequest):
    approval_code: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UnsubscribeApprovalRequestBuilder: ...

class UnsubscribeApprovalRequestBuilder:
    def __init__(self) -> None: ...
    def approval_code(self, approval_code: str) -> UnsubscribeApprovalRequestBuilder: ...
    def build(self) -> UnsubscribeApprovalRequest: ...
