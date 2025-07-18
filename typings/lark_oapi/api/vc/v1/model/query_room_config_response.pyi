from .query_room_config_response_body import QueryRoomConfigResponseBody as QueryRoomConfigResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRoomConfigResponse(BaseResponse):
    data: QueryRoomConfigResponseBody | None
    def __init__(self, d=None) -> None: ...
