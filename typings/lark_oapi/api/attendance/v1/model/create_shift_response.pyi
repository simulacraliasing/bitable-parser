from .create_shift_response_body import CreateShiftResponseBody as CreateShiftResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateShiftResponse(BaseResponse):
    data: CreateShiftResponseBody | None
    def __init__(self, d=None) -> None: ...
