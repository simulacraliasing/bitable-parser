from .get_minutes_response_body import GetMinutesResponseBody as GetMinutesResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMinutesResponse(BaseResponse):
    data: GetMinutesResponseBody | None
    def __init__(self, d=None) -> None: ...
