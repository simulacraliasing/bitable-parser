from .recognize_bank_card_response_body import RecognizeBankCardResponseBody as RecognizeBankCardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeBankCardResponse(BaseResponse):
    data: RecognizeBankCardResponseBody | None
    def __init__(self, d=None) -> None: ...
