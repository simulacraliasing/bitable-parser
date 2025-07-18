from .apply_reserve_response_body import ApplyReserveResponseBody as ApplyReserveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ApplyReserveResponse(BaseResponse):
    data: ApplyReserveResponseBody | None
    def __init__(self, d=None) -> None: ...
