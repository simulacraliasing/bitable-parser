from .recognize_id_card_response_body import RecognizeIdCardResponseBody as RecognizeIdCardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeIdCardResponse(BaseResponse):
    data: RecognizeIdCardResponseBody | None
    def __init__(self, d=None) -> None: ...
