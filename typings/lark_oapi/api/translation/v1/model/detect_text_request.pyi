from .detect_text_request_body import DetectTextRequestBody as DetectTextRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class DetectTextRequest(BaseRequest):
    request_body: DetectTextRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> DetectTextRequestBuilder: ...

class DetectTextRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: DetectTextRequestBody) -> DetectTextRequestBuilder: ...
    def build(self) -> DetectTextRequest: ...
