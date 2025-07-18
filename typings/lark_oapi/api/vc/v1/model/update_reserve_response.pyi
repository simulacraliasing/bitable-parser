from .update_reserve_response_body import UpdateReserveResponseBody as UpdateReserveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateReserveResponse(BaseResponse):
    data: UpdateReserveResponseBody | None
    def __init__(self, d=None) -> None: ...
