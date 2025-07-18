from .id_convert_card_response_body import IdConvertCardResponseBody as IdConvertCardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class IdConvertCardResponse(BaseResponse):
    data: IdConvertCardResponseBody | None
    def __init__(self, d=None) -> None: ...
