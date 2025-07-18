from .get_active_meeting_reserve_response_body import GetActiveMeetingReserveResponseBody as GetActiveMeetingReserveResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetActiveMeetingReserveResponse(BaseResponse):
    data: GetActiveMeetingReserveResponseBody | None
    def __init__(self, d=None) -> None: ...
