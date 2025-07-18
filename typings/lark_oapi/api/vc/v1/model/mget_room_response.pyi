from .mget_room_response_body import MgetRoomResponseBody as MgetRoomResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MgetRoomResponse(BaseResponse):
    data: MgetRoomResponseBody | None
    def __init__(self, d=None) -> None: ...
