from .match_entity_request_body import MatchEntityRequestBody as MatchEntityRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class MatchEntityRequest(BaseRequest):
    request_body: MatchEntityRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> MatchEntityRequestBuilder: ...

class MatchEntityRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: MatchEntityRequestBody) -> MatchEntityRequestBuilder: ...
    def build(self) -> MatchEntityRequest: ...
