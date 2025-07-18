from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListAcctItemRequest(BaseRequest):
    page_size: int | None
    page_token: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListAcctItemRequestBuilder: ...

class ListAcctItemRequestBuilder:
    def __init__(self) -> None: ...
    def page_size(self, page_size: int) -> ListAcctItemRequestBuilder: ...
    def page_token(self, page_token: str) -> ListAcctItemRequestBuilder: ...
    def build(self) -> ListAcctItemRequest: ...
