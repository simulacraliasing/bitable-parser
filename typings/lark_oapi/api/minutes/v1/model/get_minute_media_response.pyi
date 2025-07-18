from .get_minute_media_response_body import GetMinuteMediaResponseBody as GetMinuteMediaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetMinuteMediaResponse(BaseResponse):
    data: GetMinuteMediaResponseBody | None
    def __init__(self, d=None) -> None: ...
