from .create_room_response_body import CreateRoomResponseBody as CreateRoomResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateRoomResponse(BaseResponse):
    data: CreateRoomResponseBody | None
    def __init__(self, d=None) -> None: ...
