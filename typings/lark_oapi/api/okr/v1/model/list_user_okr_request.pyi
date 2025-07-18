from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListUserOkrRequest(BaseRequest):
    user_id_type: str | None
    offset: str | None
    limit: str | None
    lang: str | None
    period_ids: list[str] | None
    user_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListUserOkrRequestBuilder: ...

class ListUserOkrRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> ListUserOkrRequestBuilder: ...
    def offset(self, offset: str) -> ListUserOkrRequestBuilder: ...
    def limit(self, limit: str) -> ListUserOkrRequestBuilder: ...
    def lang(self, lang: str) -> ListUserOkrRequestBuilder: ...
    def period_ids(self, period_ids: list[str]) -> ListUserOkrRequestBuilder: ...
    def user_id(self, user_id: str) -> ListUserOkrRequestBuilder: ...
    def build(self) -> ListUserOkrRequest: ...
