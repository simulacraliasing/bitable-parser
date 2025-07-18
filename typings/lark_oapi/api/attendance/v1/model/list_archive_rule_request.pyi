from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListArchiveRuleRequest(BaseRequest):
    page_size: int | None
    page_token: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListArchiveRuleRequestBuilder: ...

class ListArchiveRuleRequestBuilder:
    def __init__(self) -> None: ...
    def page_size(self, page_size: int) -> ListArchiveRuleRequestBuilder: ...
    def page_token(self, page_token: str) -> ListArchiveRuleRequestBuilder: ...
    def build(self) -> ListArchiveRuleRequest: ...
