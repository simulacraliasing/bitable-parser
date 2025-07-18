from .reserve_scope_reserve_config_response_body import ReserveScopeReserveConfigResponseBody as ReserveScopeReserveConfigResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ReserveScopeReserveConfigResponse(BaseResponse):
    data: ReserveScopeReserveConfigResponseBody | None
    def __init__(self, d=None) -> None: ...
