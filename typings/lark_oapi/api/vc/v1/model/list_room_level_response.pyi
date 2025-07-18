from .list_room_level_response_body import ListRoomLevelResponseBody as ListRoomLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListRoomLevelResponse(BaseResponse):
    data: ListRoomLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
