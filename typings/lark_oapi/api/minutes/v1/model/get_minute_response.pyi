from .get_minute_response_body import GetMinuteResponseBody as GetMinuteResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMinuteResponse(BaseResponse):
    data: GetMinuteResponseBody | None
    def __init__(self, d=None) -> None: ...
