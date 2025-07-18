from .query_user_task_request_body import QueryUserTaskRequestBody as QueryUserTaskRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class QueryUserTaskRequest(BaseRequest):
    employee_type: str | None
    ignore_invalid_users: bool | None
    include_terminated_user: bool | None
    request_body: QueryUserTaskRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> QueryUserTaskRequestBuilder: ...

class QueryUserTaskRequestBuilder:
    def __init__(self) -> None: ...
    def employee_type(self, employee_type: str) -> QueryUserTaskRequestBuilder: ...
    def ignore_invalid_users(self, ignore_invalid_users: bool) -> QueryUserTaskRequestBuilder: ...
    def include_terminated_user(self, include_terminated_user: bool) -> QueryUserTaskRequestBuilder: ...
    def request_body(self, request_body: QueryUserTaskRequestBody) -> QueryUserTaskRequestBuilder: ...
    def build(self) -> QueryUserTaskRequest: ...
