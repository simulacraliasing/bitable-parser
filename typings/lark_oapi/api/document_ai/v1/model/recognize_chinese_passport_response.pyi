from .recognize_chinese_passport_response_body import RecognizeChinesePassportResponseBody as RecognizeChinesePassportResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeChinesePassportResponse(BaseResponse):
    data: RecognizeChinesePassportResponseBody | None
    def __init__(self, d=None) -> None: ...
