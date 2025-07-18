from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListFileLikeRequest(BaseRequest):
    file_type: str | None
    page_size: int | None
    page_token: str | None
    user_id_type: str | None
    file_token: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListFileLikeRequestBuilder: ...

class ListFileLikeRequestBuilder:
    def __init__(self) -> None: ...
    def file_type(self, file_type: str) -> ListFileLikeRequestBuilder: ...
    def page_size(self, page_size: int) -> ListFileLikeRequestBuilder: ...
    def page_token(self, page_token: str) -> ListFileLikeRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> ListFileLikeRequestBuilder: ...
    def file_token(self, file_token: str) -> ListFileLikeRequestBuilder: ...
    def build(self) -> ListFileLikeRequest: ...
