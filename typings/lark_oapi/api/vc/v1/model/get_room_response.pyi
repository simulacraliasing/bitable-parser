from .get_room_response_body import GetRoomResponseBody as GetRoomResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetRoomResponse(BaseResponse):
    data: GetRoomResponseBody | None
    def __init__(self, d=None) -> None: ...
