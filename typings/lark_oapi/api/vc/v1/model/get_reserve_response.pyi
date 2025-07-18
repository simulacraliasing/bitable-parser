from .get_reserve_response_body import GetReserveResponseBody as GetReserveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetReserveResponse(BaseResponse):
    data: GetReserveResponseBody | None
    def __init__(self, d=None) -> None: ...
