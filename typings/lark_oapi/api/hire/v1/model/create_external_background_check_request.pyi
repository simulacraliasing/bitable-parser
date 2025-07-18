from .external_background_check import ExternalBackgroundCheck as ExternalBackgroundCheck
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateExternalBackgroundCheckRequest(BaseRequest):
    request_body: ExternalBackgroundCheck | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateExternalBackgroundCheckRequestBuilder: ...

class CreateExternalBackgroundCheckRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: ExternalBackgroundCheck) -> CreateExternalBackgroundCheckRequestBuilder: ...
    def build(self) -> CreateExternalBackgroundCheckRequest: ...
