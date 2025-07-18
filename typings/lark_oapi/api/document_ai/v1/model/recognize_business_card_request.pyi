from .recognize_business_card_request_body import RecognizeBusinessCardRequestBody as RecognizeBusinessCardRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class RecognizeBusinessCardRequest(BaseRequest):
    request_body: RecognizeBusinessCardRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> RecognizeBusinessCardRequestBuilder: ...

class RecognizeBusinessCardRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: RecognizeBusinessCardRequestBody) -> RecognizeBusinessCardRequestBuilder: ...
    def build(self) -> RecognizeBusinessCardRequest: ...
