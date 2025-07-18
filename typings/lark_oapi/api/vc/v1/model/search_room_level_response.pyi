from .search_room_level_response_body import SearchRoomLevelResponseBody as SearchRoomLevelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchRoomLevelResponse(BaseResponse):
    data: SearchRoomLevelResponseBody | None
    def __init__(self, d=None) -> None: ...
