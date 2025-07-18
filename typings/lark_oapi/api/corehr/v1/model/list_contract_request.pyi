from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListContractRequest(BaseRequest):
    page_token: str | None
    page_size: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListContractRequestBuilder: ...

class ListContractRequestBuilder:
    def __init__(self) -> None: ...
    def page_token(self, page_token: str) -> ListContractRequestBuilder: ...
    def page_size(self, page_size: str) -> ListContractRequestBuilder: ...
    def build(self) -> ListContractRequest: ...
