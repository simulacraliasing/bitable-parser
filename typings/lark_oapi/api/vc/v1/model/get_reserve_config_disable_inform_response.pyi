from .get_reserve_config_disable_inform_response_body import GetReserveConfigDisableInformResponseBody as GetReserveConfigDisableInformResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetReserveConfigDisableInformResponse(BaseResponse):
    data: GetReserveConfigDisableInformResponseBody | None
    def __init__(self, d=None) -> None: ...
