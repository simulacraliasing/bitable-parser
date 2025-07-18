from .search_contract_request_body import SearchContractRequestBody as SearchContractRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class SearchContractRequest(BaseRequest):
    page_size: int | None
    page_token: str | None
    user_id_type: str | None
    request_body: SearchContractRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> SearchContractRequestBuilder: ...

class SearchContractRequestBuilder:
    def __init__(self) -> None: ...
    def page_size(self, page_size: int) -> SearchContractRequestBuilder: ...
    def page_token(self, page_token: str) -> SearchContractRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> SearchContractRequestBuilder: ...
    def request_body(self, request_body: SearchContractRequestBody) -> SearchContractRequestBuilder: ...
    def build(self) -> SearchContractRequest: ...
