from .extract_entity_request_body import ExtractEntityRequestBody as ExtractEntityRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ExtractEntityRequest(BaseRequest):
    request_body: ExtractEntityRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ExtractEntityRequestBuilder: ...

class ExtractEntityRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: ExtractEntityRequestBody) -> ExtractEntityRequestBuilder: ...
    def build(self) -> ExtractEntityRequest: ...
