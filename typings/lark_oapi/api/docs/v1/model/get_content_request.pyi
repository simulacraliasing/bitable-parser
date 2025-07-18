from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class GetContentRequest(BaseRequest):
    doc_token: str | None
    doc_type: str | None
    content_type: str | None
    lang: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> GetContentRequestBuilder: ...

class GetContentRequestBuilder:
    def __init__(self) -> None: ...
    def doc_token(self, doc_token: str) -> GetContentRequestBuilder: ...
    def doc_type(self, doc_type: str) -> GetContentRequestBuilder: ...
    def content_type(self, content_type: str) -> GetContentRequestBuilder: ...
    def lang(self, lang: str) -> GetContentRequestBuilder: ...
    def build(self) -> GetContentRequest: ...
