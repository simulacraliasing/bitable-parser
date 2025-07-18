from .create_pin_response_body import CreatePinResponseBody as CreatePinResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreatePinResponse(BaseResponse):
    data: CreatePinResponseBody | None
    def __init__(self, d=None) -> None: ...
