from .get_shift_response_body import GetShiftResponseBody as GetShiftResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetShiftResponse(BaseResponse):
    data: GetShiftResponseBody | None
    def __init__(self, d=None) -> None: ...
