from .protect_search_agency_request_body import ProtectSearchAgencyRequestBody as ProtectSearchAgencyRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ProtectSearchAgencyRequest(BaseRequest):
    request_body: ProtectSearchAgencyRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ProtectSearchAgencyRequestBuilder: ...

class ProtectSearchAgencyRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: ProtectSearchAgencyRequestBody) -> ProtectSearchAgencyRequestBuilder: ...
    def build(self) -> ProtectSearchAgencyRequest: ...
