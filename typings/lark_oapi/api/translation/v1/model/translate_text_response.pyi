from .translate_text_response_body import TranslateTextResponseBody as TranslateTextResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class TranslateTextResponse(BaseResponse):
    data: TranslateTextResponseBody | None
    def __init__(self, d=None) -> None: ...
