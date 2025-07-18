from .get_room_level_response_body import GetRoomLevelResponseBody as GetRoomLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetRoomLevelResponse(BaseResponse):
    data: GetRoomLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
