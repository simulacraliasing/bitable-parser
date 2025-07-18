from .detect_text_response_body import DetectTextResponseBody as DetectTextResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DetectTextResponse(BaseResponse):
    data: DetectTextResponseBody | None
    def __init__(self, d=None) -> None: ...
