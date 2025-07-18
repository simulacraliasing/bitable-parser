from .recognize_business_card_response_body import RecognizeBusinessCardResponseBody as RecognizeBusinessCardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeBusinessCardResponse(BaseResponse):
    data: RecognizeBusinessCardResponseBody | None
    def __init__(self, d=None) -> None: ...
