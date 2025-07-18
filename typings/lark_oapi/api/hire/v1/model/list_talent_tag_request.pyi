from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListTalentTagRequest(BaseRequest):
    keyword: str | None
    id_list: list[str] | None
    type: int | None
    include_inactive: bool | None
    page_size: int | None
    page_token: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListTalentTagRequestBuilder: ...

class ListTalentTagRequestBuilder:
    def __init__(self) -> None: ...
    def keyword(self, keyword: str) -> ListTalentTagRequestBuilder: ...
    def id_list(self, id_list: list[str]) -> ListTalentTagRequestBuilder: ...
    def type(self, type: int) -> ListTalentTagRequestBuilder: ...
    def include_inactive(self, include_inactive: bool) -> ListTalentTagRequestBuilder: ...
    def page_size(self, page_size: int) -> ListTalentTagRequestBuilder: ...
    def page_token(self, page_token: str) -> ListTalentTagRequestBuilder: ...
    def build(self) -> ListTalentTagRequest: ...
