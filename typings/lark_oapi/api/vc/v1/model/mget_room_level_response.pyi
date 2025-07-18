from .mget_room_level_response_body import MgetRoomLevelResponseBody as MgetRoomLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MgetRoomLevelResponse(BaseResponse):
    data: MgetRoomLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
