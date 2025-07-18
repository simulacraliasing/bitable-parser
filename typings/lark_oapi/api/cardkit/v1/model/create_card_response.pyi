from .create_card_response_body import CreateCardResponseBody as CreateCardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCardResponse(BaseResponse):
    data: CreateCardResponseBody | None
    def __init__(self, d=None) -> None: ...
