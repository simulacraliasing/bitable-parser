from .get_reserve_config_admin_response_body import GetReserveConfigAdminResponseBody as GetReserveConfigAdminResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetReserveConfigAdminResponse(BaseResponse):
    data: GetReserveConfigAdminResponseBody | None
    def __init__(self, d=None) -> None: ...
