from .query_user_approval_request_body import QueryUserApprovalRequestBody as QueryUserApprovalRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class QueryUserApprovalRequest(BaseRequest):
    employee_type: str | None
    request_body: QueryUserApprovalRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> QueryUserApprovalRequestBuilder: ...

class QueryUserApprovalRequestBuilder:
    def __init__(self) -> None: ...
    def employee_type(self, employee_type: str) -> QueryUserApprovalRequestBuilder: ...
    def request_body(self, request_body: QueryUserApprovalRequestBody) -> QueryUserApprovalRequestBuilder: ...
    def build(self) -> QueryUserApprovalRequest: ...
