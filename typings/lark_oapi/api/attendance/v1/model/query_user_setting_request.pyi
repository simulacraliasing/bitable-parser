from .query_user_setting_request_body import QueryUserSettingRequestBody as QueryUserSettingRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class QueryUserSettingRequest(BaseRequest):
    employee_type: str | None
    request_body: QueryUserSettingRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> QueryUserSettingRequestBuilder: ...

class QueryUserSettingRequestBuilder:
    def __init__(self) -> None: ...
    def employee_type(self, employee_type: str) -> QueryUserSettingRequestBuilder: ...
    def request_body(self, request_body: QueryUserSettingRequestBody) -> QueryUserSettingRequestBuilder: ...
    def build(self) -> QueryUserSettingRequest: ...
