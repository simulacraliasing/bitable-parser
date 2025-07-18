from .get_reserve_config_form_response_body import GetReserveConfigFormResponseBody as GetReserveConfigFormResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetReserveConfigFormResponse(BaseResponse):
    data: GetReserveConfigFormResponseBody | None
    def __init__(self, d=None) -> None: ...
