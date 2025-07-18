from .recognize_food_produce_license_request_body import RecognizeFoodProduceLicenseRequestBody as RecognizeFoodProduceLicenseRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class RecognizeFoodProduceLicenseRequest(BaseRequest):
    request_body: RecognizeFoodProduceLicenseRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> RecognizeFoodProduceLicenseRequestBuilder: ...

class RecognizeFoodProduceLicenseRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: RecognizeFoodProduceLicenseRequestBody) -> RecognizeFoodProduceLicenseRequestBuilder: ...
    def build(self) -> RecognizeFoodProduceLicenseRequest: ...
