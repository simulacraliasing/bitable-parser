from .list_room_response_body import ListRoomResponseBody as ListRoomResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListRoomResponse(BaseResponse):
    data: ListRoomResponseBody | None
    def __init__(self, d=None) -> None: ...
