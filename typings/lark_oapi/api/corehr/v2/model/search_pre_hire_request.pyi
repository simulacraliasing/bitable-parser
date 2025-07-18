from .search_pre_hire_request_body import SearchPreHireRequestBody as SearchPreHireRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class SearchPreHireRequest(BaseRequest):
    page_size: int | None
    page_token: str | None
    user_id_type: str | None
    department_id_type: str | None
    request_body: SearchPreHireRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> SearchPreHireRequestBuilder: ...

class SearchPreHireRequestBuilder:
    def __init__(self) -> None: ...
    def page_size(self, page_size: int) -> SearchPreHireRequestBuilder: ...
    def page_token(self, page_token: str) -> SearchPreHireRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> SearchPreHireRequestBuilder: ...
    def department_id_type(self, department_id_type: str) -> SearchPreHireRequestBuilder: ...
    def request_body(self, request_body: SearchPreHireRequestBody) -> SearchPreHireRequestBuilder: ...
    def build(self) -> SearchPreHireRequest: ...
