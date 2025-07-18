from .search_room_response_body import SearchRoomResponseBody as SearchRoomResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchRoomResponse(BaseResponse):
    data: SearchRoomResponseBody | None
    def __init__(self, d=None) -> None: ...
